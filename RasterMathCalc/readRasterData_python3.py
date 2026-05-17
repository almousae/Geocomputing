from osgeo import gdal
#import osgeo.gdal


dataset =gdal.Open('landsat\L71026029_02920000609_B30_CLIP.TIF',gdal.GA_ReadOnly)

#basic info for the driver
print (dataset.GetDriver().ShortName)
print (dataset.GetDriver().LongName)

#get the Metadata
print (dataset.GetMetadata())

#Fetch the number of raster bands on this dataset.
band_count=dataset.RasterCount

#Get the number of columns and rows
cols = dataset.RasterXSize
rows = dataset.RasterYSize

print ('dataset band count, numbers of rows and columns:',band_count,rows,cols)

#get projection
print (dataset.GetProjection())

# Get raster georeference info
geotransform = dataset.GetGeoTransform()
if geotransform:
    xOrigin = geotransform[0]
    yOrigin = geotransform[3]
    pixelWidth = geotransform[1]
    pixelHeight = geotransform[5]
    print ("Origin = ({}, {})", xOrigin, yOrigin)
    print ("Pixel Size = ({}, {})", pixelWidth,pixelHeight)

