# Himalayan Medicinal Plant Biodiversity


Period-wise range shift estimation and future distribution using shared socio-economic pathway on Taxus wallichiana medicinal plant

This repository contains code and instructions for estimating probabilistic niche distribution of Taxus wallichiana driven by shared socio-economic pathways guided climate change performing using R.

Authors: Dhriti Chakraborty, Kartick Chandra Mondal, Somnath Mukhopadhyay.

Table of Contents:

* Introduction

* System Prerequisites

* Installation

* Data Description

* Assessment of suitable habitat

* References

# Introduction

Assessment of the effect of climate change on the distribution of suitable habitat of Taxus wallichiana is done through the estimation of probabilistic niche under different climatic scenarios. This is done through ensemble species distribution modeling which combines several prediction models. Each model predicts the probability of the occurrence of the species based on the relation between the presence absence data with the explanatory dataset of the occurrence points. This manual guides you through the process of performing the estimation of period wise species distribution using eSDM  in R. 

# System Prerequisites

Before using this code, ensure that the following prerequisites are needed to be installed:

• R: It can be downloaded and installed from the official website: https://www.r-project.org/

• RStudio: RStudio is an integrated development environment (IDE) for R. It provides a user-friendly interface and additional tools for R programming. RStudio can be downloaded and installed from the official website: https://www.rstudio.com/.

# Installation

To use this code, follow these steps:

1. Download the ZIP file and extract it.

2. Open the R environment or RStudio.

3. Set the working directory to the location where it is cloned or extracted from the repository.

4. Install the required R packages by running the following command in the R console: For e.g.

install.packages(c("dplyr", "tidyr", "mapview", "corrplot", "usdm"))

# Data Description

Two required datasets are:

1. Species Occurrence Dataset: We gather the species occurrence data from free online source: https://www.gbif.org/.

2. Explanatory Dataset: We consider the bioclimatic variables and elevation as explanatory variables to assess the effect of climate change. This data is downloaded from: https://www.worldclim.org/.

# Assessment of suitable habitat

Assessment of probabilistic niche distribution and it’s period wise change include the following change:

1. Open the code_t.wallichiana file in the R environment.

2. Build the data frame consisting of the presence absence data in binary and explanatory variables of occurrence point.

3. Perform multicollinearity test and remove highly collinear variables.

4. Assess the relative variable importances to understand the ecological response of the species.

5. Predict a probabilistic suitable niche using seven participating models and combine their outcome as the ensemble model.

6. Check the efficacy of the ensemble model in terms of AUC and TSS.

7. Go for probabilistic niche distribution projection for current as well as different future climatic scenarios for different periods.

8. Estimate the change in the habitat suitability by the assessment of the difference in the probability of occurrence between two successive period.

# References

[1] Naimi B, Ara’ujo MB (2016) sdm: a reproducible and extensible r platform forspecies distribution modelling. Ecography 3#9(4):368–375

[2] Naimi B, Hamm NA, Groen TA, et al (2014) Where is positional uncertainty a problem for species distribution modelling? Ecography 37(2):191–203

[3] RStudio T, et al (2020) Rstudio: integrated development for r. Rstudio Team, PBC, Boston, MA URL http://www rstudio com
