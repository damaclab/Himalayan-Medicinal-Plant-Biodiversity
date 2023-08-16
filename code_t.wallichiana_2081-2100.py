
#2081to2100
#ssp126
bio_future4_1=raster::stack("D:/worldclim_data/Future_data/2081-2100/wc2.1_10m_bioc_BCC-CSM2-MR_ssp126_2081-2100.tif")
bio_future4_1
biof_new4_1 = crop(bio_future4_1,extent(ele_new))
bio_fu4_1 <- addLayer(biof_new4_1, ele_new)
plot(bio_fu4_1[[1]])
names(bio_fu4_1) <- names(bio)
ens4_1 <- ensemble(m, bio_fu4_1, filename='rgqm.img',setting=list(method='weighted',stat='tss',opt=2))
cl4_1 <- colorRampPalette(c('darkred','red','gray','green','blue'))
plot(ens4_1, col=cl4_1(200),xlim=c(57,152),ylim=c(-10,63))
diff4_1 <- ens4_1 - ens3_1
cl4_1_n <- colorRampPalette(c('darkred','red','white','darkgray','green'))
plot(diff4_1, col=cl4_1_n(200),xlim=c(57,152),ylim=c(-10,63))

#ssp245
bio_future4_2=raster::stack("D:/worldclim_data/Future_data/2081-2100/wc2.1_10m_bioc_BCC-CSM2-MR_ssp245_2081-2100.tif")
bio_future4_2
biof_new4_2 = crop(bio_future4_2,extent(ele_new))
bio_fu4_2 <- addLayer(biof_new4_2, ele_new)
names(bio_fu4_2) <- names(bio)
ens4_2 <- ensemble(m, bio_fu4_2, filename='vaxjm.img',setting=list(method='weighted',stat='tss',opt=2))
cl4_2 <- colorRampPalette(c('darkred','red','gray','green','blue'))
plot(ens4_2, col=cl4_2(200),xlim=c(57,152),ylim=c(-10,63))
diff4_2 <- ens4_2 - ens3_2
cl4_2_n <- colorRampPalette(c('black','darkred','red','white','darkgray','green'))
plot(diff4_2, col=cl4_2_n(200),xlim=c(57,152),ylim=c(-10,63))

#ssp370
bio_future4_3=raster::stack("D:/worldclim_data/Future_data/2081-2100/wc2.1_10m_bioc_BCC-CSM2-MR_ssp370_2081-2100.tif")
bio_future4_3
biof_new4_3 = crop(bio_future4_3,extent(ele_new))
bio_fu4_3 <- addLayer(biof_new4_3, ele_new)
names(bio_fu4_3) <- names(bio)
ens4_3 <- ensemble(m, bio_fu4_3, filename='rcqkj.img',setting=list(method='weighted',stat='tss',opt=2))
cl4_3 <- colorRampPalette(c('darkred','red','gray','green','blue'))
plot(ens4_3, col=cl4_3(200),xlim=c(57,152),ylim=c(-10,63))
diff4_3 <- ens4_3 - ens3_3
cl4_3_n <- colorRampPalette(c('black','darkred','red','white','darkgray','green'))
plot(diff4_3, col=cl4_3_n(200),xlim=c(57,152),ylim=c(-10,63))


cl <- colorRampPalette(c('#3E49BB','#3498DB','yellow','orange','red','darkred'))
plot(ens, col=cl(200))
plot(ens2, col=cl(200))
plot(ens3, col=cl(200))
plot(ens4, col=cl(200))
plot(ens5, col=cl(200))
proj4string(spg3) <- projection(ens)
library(mapview)
mapview(ens,col.regions=cl(200)) + spg3
ch4 <- ens4 - ens
cl2 <- colorRampPalette(c('red','orange','yellow','gray','green','blue'))
plot(ch4,col=cl2(200))

#ssp585
bio_future4_4=raster::stack("D:/worldclim_data/Future_data/2081-2100/wc2.1_10m_bioc_BCC-CSM2-MR_ssp585_2081-2100.tif")
bio_future4_4
biof_new4_4 = crop(bio_future4_4,extent(ele_new))
bio_fu4_4 <- addLayer(biof_new4_4, ele_new)
plot(bio_fu4_4[[1]])
names(bio_fu4_4) <- names(bio)
ens4_4 <- ensemble(m, bio_fu4_4, filename='rxoxxjm.img',setting=list(method='weighted',stat='tss',opt=2))
cl4_4 <- colorRampPalette(c('darkred','red','gray','green','blue'))
plot(ens4_4, col=cl4_4(200),xlim=c(57,152),ylim=c(-10,63))
diff4_4 <- ens4_4 - ens3_4
cl4_4_n <- colorRampPalette(c('black','darkred','red','white','darkgray','green'))
plot(diff4_4, col=cl4_4_n(200),xlim=c(57,152),ylim=c(-10,63))