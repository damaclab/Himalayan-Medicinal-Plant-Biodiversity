#2021to2040
#ssp126
bio_future1_1=raster::stack("D:/worldclim_data/Future_data/2020-2040-20220807T153059Z-001/2020-2040/wc2.1_10m_bioc_BCC-CSM2-MR_ssp126_2021-2040.tif")
bio_future1_1
biof_new1_1 = crop(bio_future1_1,extent(ele_new))
bio_fu1_1 <- addLayer(biof_new1_1, ele_new)
plot(bio_fu1_1[[1]])
names(bio_fu1_1)<- names(bio)
bio_fu1_1
ens1_1 <- ensemble(m, bio_fu1_1, filename='gmvk.img',setting=list(method='weighted',stat='tss',opt=2))
cl1_1 <- colorRampPalette(c('darkred','red','gray','green','blue'))
plot(ens1_1, col=cl1_1(200),xlim=c(57,152),ylim=c(-10,63))
diff1 <- ens1_1 - ens
cl1_1_n <- colorRampPalette(c('red','white','darkgray','green','darkgreen'))
plot(diff1, col=cl1_1_n(200),xlim=c(57,152),ylim=c(-10,63))


#ssp245
bio_future1_2=raster::stack("D:/worldclim_data/Future_data/2020-2040-20220807T153059Z-001/2020-2040/wc2.1_10m_bioc_BCC-CSM2-MR_ssp245_2021-2040 (1).tif")
bio_future1_2
biof_new1_2 = crop(bio_future1_2,extent(ele_new))
bio_fu1_2 <- addLayer(biof_new1_2, ele_new)
plot(bio_fu1_2[[1]])
names(bio_fu1_2)<- names(bio)
bio_fu1_2
ens1_2 <- ensemble(m, bio_fu1_2, filename='gvzx.img',setting=list(method='weighted',stat='tss',opt=2))
cl1_2 <- colorRampPalette(c('darkred','red','gray','green','blue'))
plot(ens1_2, col=cl1_2(200),xlim=c(57,152),ylim=c(-10,63))
diff1_2 <- ens1_2 - ens
cl1_2_n <- colorRampPalette(c('red','white','darkgray','green','darkgreen'))
plot(diff1_2, col=cl1_2_n(200),xlim=c(57,152),ylim=c(-10,63))

#ssp370
bio_future1_3=raster::stack("D:/worldclim_data/Future_data/NEW_future_bcc_tn_tr_pr_bc_10min_ssp370_20to40/wc2.1_10m_bioc_BCC-CSM2-MR_ssp245_2021-2040.tif")
bio_future1_3
biof_new = crop(bio_future,extent(ele_new))
bio_fu <- addLayer(biof_new, ele_new)
plot(bio_fu[[1]])
names(bio_fu)<- names(bio)
bio_fu
ens1_3 <- ensemble(m, bio_fu, filename='gnmoj.img',setting=list(method='weighted',stat='tss',opt=2))
cl1_3 <- colorRampPalette(c('darkred','red','gray','green','blue'))
plot(ens1_3, col=cl1_3(200),xlim=c(57,152),ylim=c(-10,63))
diff1_3 <- ens1_3 - ens
cl1_3_n <- colorRampPalette(c('red','white','darkgray','green','darkgreen'))
plot(diff1_3, col=cl1_3_n(200),xlim=c(57,152),ylim=c(-10,63))


cl <- colorRampPalette(c('#3E49BB','#3498DB','yellow','orange','red','darkred'))
plot(ens, col=cl(200))
plot(ens2, col=cl(200))
proj4string(spg3) <- projection(ens)
library(mapview)
mapview(ens,col.regions=cl(200)) + spg3
ch <- ens2 - ens
cl2 <- colorRampPalette(c('red','orange','yellow','gray','green','blue'))
plot(ch,col=cl2(200))

#ssp585
bio_future1_4=raster::stack("D:/worldclim_data/Future_data/2020-2040-20220807T153059Z-001/2020-2040/wc2.1_10m_bioc_BCC-CSM2-MR_ssp585_2021-2040.tif")
bio_future1_4
biof_new1_4 = crop(bio_future1_4,extent(ele_new))
bio_fu1_4 <- addLayer(biof_new1_4, ele_new)
plot(bio_fu1_4[[1]])
names(bio_fu1_4)<- names(bio)
bio_fu1_4
ens1_4 <- ensemble(m, bio_fu1_4, filename='nozj.img',setting=list(method='weighted',stat='tss',opt=2))
cl1_4 <- colorRampPalette(c('darkred','red','gray','green','blue'))
plot(ens1_4, col=cl1_4(200),xlim=c(57,152),ylim=c(-10,63))
diff1_4 <- ens1_4 - ens
cl1_4_n <- colorRampPalette(c('darkred','red','white','darkgray','green','darkgreen'))
plot(diff1_4, col=cl1_4_n(200),xlim=c(57,152),ylim=c(-10,63))
