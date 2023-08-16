  
#2061to2080
#ssp126
bio_future3_1 =raster::stack("D:/worldclim_data/Future_data/2061-2080/wc2.1_10m_bioc_BCC-CSM2-MR_ssp126_2061-2080.tif")
bio_future3_1
biof_new3_1 = crop(bio_future3_1,extent(ele_new))
bio_fu3_1 <- addLayer(biof_new3_1, ele_new)
plot(bio_fu3_1[[1]])
names(bio_fu3_1) <- names(bio)
ens3_1 <- ensemble(m, bio_fu3_1, filename='fsjgj.img',setting=list(method='weighted',stat='tss',opt=2))
cl3_1 <- colorRampPalette(c('darkred','red','gray','green','blue'))
plot(ens3_1, col=cl3_1(200),xlim=c(57,152),ylim=c(-10,63))
diff3_1 <- ens3_1 - ens2_1
cl3_1_n <- colorRampPalette(c('darkred','red','white','darkgray','green'))
plot(diff3_1, col=cl3_1_n(200),xlim=c(57,152),ylim=c(-10,63))
  
#ssp245
bio_future3_2=raster::stack("D:/worldclim_data/Future_data/2061-2080/wc2.1_10m_bioc_BCC-CSM2-MR_ssp245_2061-2080.tif")
bio_future3_2
biof_new3_2 = crop(bio_future3_2,extent(ele_new))
bio_fu3_2 <- addLayer(biof_new3_2, ele_new)
plot(bio_fu3_2[[1]])
names(bio_fu3_2) <- names(bio)
ens3_2 <- ensemble(m, bio_fu3_2, filename='xuljm.img',setting=list(method='weighted',stat='tss',opt=2))
cl3_2 <- colorRampPalette(c('darkred','red','gray','green','blue'))
plot(ens3_2, col=cl3_2(200),xlim=c(57,152),ylim=c(-10,63))
diff3_2 <- ens3_2 - ens2_2
cl3_2_n <- colorRampPalette(c('darkred','red','white','darkgray','green'))
plot(diff3_2, col=cl3_2_n(200),xlim=c(57,152),ylim=c(-10,63))
  
#ssp370
bio_future3_3=raster::stack("D:/worldclim_data/Future_data/2061-2080/wc2.1_10m_bioc_BCC-CSM2-MR_ssp370_2061-2080.tif")
bio_future3_3
biof_new3_3 = crop(bio_future3_3,extent(ele_new))
bio_fu3_3 <- addLayer(biof_new3_3, ele_new)
plot(bio_fu3_3[[1]])
names(bio_fu3_3) <- names(bio)
ens3_3 <- ensemble(m, bio_fu3_3, filename='powjm.img',setting=list(method='weighted',stat='tss',opt=2))
cl3_3 <- colorRampPalette(c('darkred','red','gray','green','blue'))
plot(ens3_3, col=cl3_3(200),xlim=c(57,152),ylim=c(-10,63))
diff3_3 <- ens3_3 - ens2_3
cl3_3_n <- colorRampPalette(c('darkred','red','white','darkgray','green'))
plot(diff3_3, col=cl3_3_n(200),xlim=c(57,152),ylim=c(-10,63))


d<- ens2_3 - ens3_3
d1<- diff3_3-ens1_3
plot(d1, col=cl3_3(200),xlim=c(57,152),ylim=c(-10,63))
plot(d, col=cl3_3(200),xlim=c(57,152),ylim=c(-10,63))
plot(diff3_3, col=cl3_3(200),xlim=c(57,152),ylim=c(-10,63))


cl <- colorRampPalette(c('#3E49BB','#3498DB','yellow','orange','red','darkred'))
plot(ens, col=cl(200))
plot(ens2, col=cl(200))
plot(ens3, col=cl(200))
plot(ens4, col=cl(200))
proj4string(spg3) <- projection(ens)
library(mapview)
mapview(ens,col.regions=cl(200)) + spg3
ch4 <- ens4 - ens
cl2 <- colorRampPalette(c('red','orange','yellow','gray','green','blue'))
plot(ch4,col=cl2(200))
proj4string(spg3) <- projection(ens2)
library(mapview)
mapview(ens2,col.regions=cl(200)) + spg3
ch23 <- ens3 - ens2
cl2 <- colorRampPalette(c('red','orange','yellow','gray','green','blue'))
plot(ch23,col=cl2(200))

#ssp585
bio_future3_4=raster::stack("D:/worldclim_data/Future_data/2061-2080/wc2.1_10m_bioc_BCC-CSM2-MR_ssp585_2061-2080.tif")
bio_future3_4
biof_new3_4 = crop(bio_future3_4,extent(ele_new))
bio_fu3_4 <- addLayer(biof_new3_4, ele_new)
plot(bio_fu3_4[[1]])
names(bio_fu3_4) <- names(bio)
ens3_4 <- ensemble(m, bio_fu3_4, filename='fafkjm.img',setting=list(method='weighted',stat='tss',opt=2))
cl3_4 <- colorRampPalette(c('darkred','red','gray','green','blue'))
plot(ens3_4, col=cl3_4(200),xlim=c(57,152),ylim=c(-10,63))
diff3_4 <- ens3_4 - ens2_4
cl3_4_n <- colorRampPalette(c('darkred','red','white','darkgray','green','darkgreen'))
plot(diff3_4, col=cl3_4_n(200),xlim=c(57,152),ylim=c(-10,63))