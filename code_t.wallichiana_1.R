library(sdm)
library(dismo)
install.packages("dplyr")
library(dplyr)
install.packages("tidyr")
library(tidyr)
install.packages("mapview")
library(mapview)
install.packages("corrplot")
library(corrplot)


gbif("Taxus","wallichiana",download= F)
sp3 <- gbif("Taxus","wallichiana",download= T)
class(sp3)
dim(sp3)
table(sp3$basisOfRecord)
sp3 <- sp3 %>% 
  filter(basisOfRecord %in% c("HUMAN_OBSERVATION","OBSERVATION","PRESERVED_SPECIMEN"))
nrow(sp3)
spg3 = sp3 %>% select(lon,lat)
spg3$species <- 1
spg3 <- spg3 %>% drop_na()
nrow(spg3)
class(spg3)
coordinates(spg3) <- c('lon','lat')
spg3
ele=raster::stack("D:/worldclim_data/Elevation/wc2.1_10m_elev/elevation.tif")
ele
plot(ele)
plot(ele,xlim=c(60,120),ylim=c(0,47))
cl1 <- colorRampPalette(c('#87CEFA','green','yellow','orange','red','darkred'))
plot(ele, col=cl1(200),xlim=c(55,130),ylim=c(-10,49))
points(spg3)


bioclim <- raster::getData('worldclim', var='bio', res=10)
bioclim
ele_new = crop(ele,extent(bioclim))
bio <- addLayer(bioclim, ele_new)
bio
names(bio)
head(bio)
plot(bio[[1]]) 
points(spg3)

e <- drawExtent()
spg3 <- crop(spg3, e)
spg3
points(spg3,col='red')
bioc <- crop(bio, e)
bioc
head.matrix(bioc)

library(usdm)
vif(bioc)
ex <- raster::extract(bioc,spg3)
head(ex)
head.matrix(ex,n=100L,)

#corrplot
M1<-cor(ex)
head(round(M1,2))
corrplot(M1, method="circle")


v <- vifstep(ex)
v
#vifcor
bioc <- exclude(bioc, v)
bioc

library(sdm)
d <- sdmData(species~., spg3, predictors= bioc, bg = list(method='gRandom',n=1000))
d
getmethodNames()
library(parallel)
m <- sdm(species~., d, methods=c('glm','gam','rf','maxent','mars','fda','cart'), replication=c('sub','boot'),
         test.p=30,n=3, parallelSetting=list(ncore=6,method='parallel'))
m

installAll()
install.packages("shiny")
library(shiny)
library(shinyBS)
gui(m)
p1 <- predict(m, bio,filename='mfkutlm.img')
p1
names(p1)
plot(p1[[c(1,4,7,10,13,16,19,22,25,28,31,34,37,40)]])
ens <- ensemble(m, p1, filename='mxcyoec.img',setting=list(method='weighted',stat='tss',opt=2))
ens
plot(ens)
View(ens)
plot(ens,xlim=c(57,152),ylim=c(-10,63))
cl <- colorRampPalette(c('darkred','red','gray','green','blue'))
plot(ens, col=cl(400),xlim=c(57,152),ylim=c(-10,63))