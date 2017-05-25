pro calculate_dem_1d,tt,aia_file_format,demreg_path,x1,x2,y1,y2,dt,logtemps,mlogt,dem,edem,dn,edn,tr_logt,TRmatrix
;~~~~~~~~
;Read in all channel data from FITS files into the array aia_cube for a given timestamp (requires SSW)
aia_files = findfile(aia_file_format)
aia_files = shift(aia_files,1)
print,aia_files
read_sdo,aia_files,ind,data

;------------
;Cut out the appropriate portion of the map
print,'Using the pixel-averaged counts around x = ',x1,x2,', y = ',y1,y2
dn = fltarr(n_elements(ind))
foreach el,ind,i do begin 
    tmp = data[x1:x2,y1:y2,i]
    dn[i] = mean(tmp)
endforeach

;------------
;Decide on temperature array
; These are the bin edges
temps=10d^tt
logtemps=alog10(temps)
; This is is the temperature bin mid-points
mlogt=get_edges(logtemps,/mean)

;------------
;Response functions
;Restore AIA response functions
restore,file=demreg_path + 'idl/aia_resp.dat'
; Only want the coronal ones without 304A
idc=[0,1,2,3,4,6]
tr_logt=tresp.logte
; Don't need the response outside of the T range we want for the DEM
gdt=where(tr_logt ge min(logtemps) and tr_logt le max(logtemps),ngd)
tr_logt=tr_logt[gdt]
TRmatrix=tresp.all[*,idc]
TRmatrix=TRmatrix[gdt,*]

;---------------
;Errors--I don't really understand what is going on here...
nf=n_elements(dn)
; workout the error on the data
edn_in=fltarr(nf)
gains=[18.3,17.6,17.7,18.3,18.3,17.6]
dn2ph=gains*[94,131,171,193,211,335]/3397.
rdnse=[1.14,1.18,1.15,1.20,1.20,1.18]
; assume all obs were 2.9s long
; but ours are 10 s long...
dn0=dn*dt
shotnoise=sqrt(dn2ph*dn0)/dn2ph/dt
; error in DN/s/px
edn=sqrt(rdnse^2+shotnoise^2)

;-----------------
;Inversion
dn2dem_pos_nb, dn, edn,TRmatrix,tr_logt,temps,dem,edem,elogt,chisq,dn_reg,/timed;,/gloci,glcindx=[0,1,1,1,1,1]
end