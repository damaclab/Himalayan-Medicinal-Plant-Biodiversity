#2041to2060
#ssp126
bio_future2_1=raster::stack("D:/worldclim_data/Future_data/2041-2060/wc2.1_10m_bioc_BCC-CSM2-MR_ssp126_2041-2060.tif")
bio_future2_1
biof_new2_1 = crop(bio_future2_1,extent(ele_new))
bio_fu2_1 <- addLayer(biof_new2_1, ele_new)
plot(bio_fu2_1[[1]])
names(bio_fu2_1) <- names(bio)
ens2_1 <- ensemble(m, bio_fu2_1, filename='dqejm.img',setting=list(method='weighted',stat='tss',opt=2))
plot(ens2_1)
cl2_1 <- colorRampPalette(c('darkred','red','gray','green','blue'))
plot(ens2_1, col=cl2_1(200),xlim=c(57,152),ylim=c(-10,63))
diff2_1 <- ens2_1 - ens1_1
cl2_1_n <- colorRampPalette(c('black','darkred','red','white','darkgray','green'))
plot(diff2_1, col=cl2_1_n(200),xlim=c(57,152),ylim=c(-10,63))

#ssp245
bio_future2_2=raster::stack("D:/worldclim_data/Future_data/2041-2060/wc2.1_10m_bioc_BCC-CSM2-MR_ssp245_2041-2060.tif")
bio_future2_2
biof_new2_2 = crop(bio_future2_2,extent(ele_new))
bio_fu2_2 <- addLayer(biof_new2_2, ele_new)
plot(bio_fu2_2[[1]])
names(bio_fu2_2) <- names(bio)
ens2_2 <- ensemble(m, bio_fu2_2, filename='jqwjm.img',setting=list(method='weighted',stat='tss',opt=2))
cl2_2 <- colorRampPalette(c('darkred','red','gray','green','blue'))
plot(ens2_2, col=cl2_2(200),xlim=c(57,152),ylim=c(-10,63))
diff2_2 <- ens2_2 - ens1_2
cl2_2_n <- colorRampPalette(c('black','darkred','red','white','darkgray','green'))
plot(diff2_2, col=cl2_2_n(200),xlim=c(57,152),ylim=c(-10,63))

#ssp370
bio_future2_3=raster::stack("D:/worldclim_data/Future_data/future_bcc_tn_tr_pr_bc_10min_ssp370/10min/wc2.1_10m_bioc_BCC-CSM2-MR_ssp370_2041-2060.tif")
bio_future2_3
biof_new2_3 = crop(bio_future2_3,extent(ele_new))
bio_fu2_3 <- addLayer(biof_new2_3, ele_new)
plot(bio_fu3[[1]])
names(bio_fu3) <- names(bio)
ens2_3 <- ensemble(m, bio_fu3, filename='joyxjm.img',setting=list(method='weighted',stat='tss',opt=2))
cl2_3 <- colorRampPalette(c('darkred','red','gray','green','blue'))
plot(ens2_3, col=cl2_3(200),xlim=c(57,152),ylim=c(-10,63))
diff2_3 <- ens2_3 - ens1_3
cl2_3_n <- colorRampPalette(c('black','darkred','red','white','darkgray','green'))
plot(diff2_3, col=cl2_3_n(200),xlim=c(57,152),ylim=c(-10,63))



cl <- colorRampPalette(c('#3E49BB','#3498DB','yellow','orange','red','darkred'))
plot(ens, col=cl(200))
plot(ens2, col=cl(200))
plot(ens3, col=cl(200))
proj4string(spg3) <- projection(ens)
library(mapview)
mapview(ens,col.regions=cl(200)) + spg3
ch3 <- ens3 - ens
cl2 <- colorRampPalette(c('red','orange','yellow','gray','green','blue'))
plot(ch3,col=cl2(200))
proj4string(spg3) <- projection(ens2)
library(mapview)
mapview(ens2,col.regions=cl(200)) + spg3
ch23 <- ens3 - ens2
cl2 <- colorRampPalette(c('red','orange','yellow','gray','green','blue'))
plot(ch23,col=cl2(200))

#ssp585
bio_future2_4=raster::stack("D:/worldclim_data/Future_data/2041-2060/wc2.1_10m_bioc_BCC-CSM2-MR_ssp585_2041-2060.tif")
bio_future2_4
biof_new2_4 = crop(bio_future2_4,extent(ele_new))
bio_fu2_4 <- addLayer(biof_new2_4, ele_new)
plot(bio_fu2_4[[1]])
names(bio_fu2_4) <- names(bio)
ens2_4 <- ensemble(m, bio_fu2_4, filename='qwjpjm.img',setting=list(method='weighted',stat='tss',opt=2))
cl2_4 <- colorRampPalette(c('darkred','red','gray','green','blue'))
plot(ens2_4, col=cl2_4(200),xlim=c(57,152),ylim=c(-10,63))
diff2_4_n <- ens2_4 - ens1_4
cl2_4_n <- colorRampPalette(c('black','darkred','red','white','darkgray','green'))
plot(diff2_4_n, col=cl2_4_n(200),xlim=c(57,152),ylim=c(-10,63))