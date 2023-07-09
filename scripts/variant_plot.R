library(tidyverse)
library(RColorBrewer)
library(pheatmap)
library(janitor)

#import data 
var_df <- read_table('./data/matrix_min11074_ratio.txt')
var_df

# simplify sample names 
var_df_name <- var_df %>%
  rename(
    `1160` = `Variants:_1160.trimmed.rg.sorted_-_hCoV-19/Wuhan/WIV04/2019|EPI_ISL_402124|2019-12-30_GISAID_REF_SEQ_2`,
    `1240` = `Variants:_1240.trimmed.rg.sorted_-_hCoV-19/Wuhan/WIV04/2019|EPI_ISL_402124|2019-12-30_GISAID_REF_SEQ`,
    `1409` = `Variants:_1409.trimmed.rg.sorted_-_hCoV-19/Wuhan/WIV04/2019|EPI_ISL_402124|2019-12-30_GISAID_REF_SEQ`,
    `1428` = `Variants:_1428.trimmed.rg.sorted_-_hCoV-19/Wuhan/WIV04/2019|EPI_ISL_402124|2019-12-30_GISAID_REF_SEQ`,
    `1463` = `Variants:_1463.trimmed.rg.sorted_-_hCoV-19/Wuhan/WIV04/2019|EPI_ISL_402124|2019-12-30_GISAID_REF_SEQ`,
    `151` = `Variants:_151.trimmed.rg.sorted_-_hCoV-19/Wuhan/WIV04/2019|EPI_ISL_402124|2019-12-30_GISAID_REF_SEQ`
  ) %>% 
  mutate(POS = as.character(POS)) %>% 
  as.data.frame() %>% 
  unite('temp_cat_ID', POS:ALT, sep = "/", remove = FALSE) %>% 
  mutate(across('temp_cat_ID', str_replace, '/', ':'))

#extract annotation table for pheatmap 
var_df_name_ann <- var_df_name %>% 
  column_to_rownames('temp_cat_ID') %>% 
  select(3) %>% 
  t()

#extract numeric table for pheatmap 
var_df_name_num <- var_df_name %>% 
  column_to_rownames('temp_cat_ID') %>% 
  select(5:10) %>% 
  t() #%>% as.data.frame()
  
#import annotation data 
hm_col_ann <- read_table('data/col_ann.txt') %>% remove_rownames %>% column_to_rownames(var="ID") #col
hm_row_ann <- var_df_name %>% select(1,5) %>% as.data.frame() %>% remove_rownames %>% column_to_rownames(var="temp_cat_ID") # col#%>% row_to_names(row_number = 1)

#plot heatmap
hm <- pheatmap(var_df_name_num,
         #annotation_row = hm_col_ann,
         annotation_col = hm_row_ann,
         gaps_row = 4,
         cluster_col = FALSE,
         cluster_rows = FALSE,
         cellwidth = 10,
         cellheight = 10,
         treeheight_col = 3,
         cutree_row = 5,
         color = blues9,
         border_color = '#d3d3d3',
         filename = './data/heatmap.tiff',
         width = 14, 
         height = 4,
         #legend formatting
         legend_labels = TRUE,
         drop_levels = TRUE
        )
