
from osgeo import gdal
import numpy
import matplotlib.pyplot as plt
from osgeo import osr


#Use array2raster function to convert ndvi_array later from main function
def array2raster(newRasterFileName,rasterOrigin,pixelWidth,pixelHeight,array):
     #Step 1-- choose a driver
     outformat = 'GTiff'
     outDriver = gdal.GetDriverByName(outformat) 

     # Create output dataset using that driver
     rows  = array.shape[0] 
     cols    = array.shape[1]
     print ('rows: ', rows, ' cols: ', cols)
     nBands   = 1
     dataType = gdal.GDT_Float32
     dsOut=outDriver.Create(newRasterFileName,cols,rows,nBands,dataType)

     # Set Geotransform
     xCorner=rasterOrigin[0]
     yCorner=rasterOrigin[1]
     xOffset=0
     yOffset=0 
     geoT = [ xCorner, pixelWidth, xOffset, yCorner, yOffset, -pixelHeight]
     dsOut.SetGeoTransform( geoT )

     # Set Projection
     mySrs = osr.SpatialReference()
     #mySrs.SetWellKnownGeogCS("WGS84")
     mySrs.ImportFromEPSG(4326) #WGS84 http://spatialreference.org/ref/epsg/
     myWKT = mySrs.ExportToWkt()
     #print myWKT
     dsOut.SetProjection(myWKT)

     # Process Each Band 
     outband = dsOut.GetRasterBand(1)
     outband.SetColorInterpretation(gdal.GCI_Undefined)
     outband.WriteArray(array)
     outband.FlushCache()

     # Close the output data 
     dsOut=None


#create a main function
if __name__ == "__main__":
    #read raster data
    
    #assign infred dataset to landsat B30 found in file
    dataset30 =gdal.Open('landsat\L71026029_02920000609_B30_CLIP.TIF',gdal.GA_ReadOnly)
    #assign red dataset to landat B40
    dataset40 =gdal.Open('landsat\L71026029_02920000609_B40_CLIP.TIF',gdal.GA_ReadOnly)

    #read Raster data as two-dimensional array 
    print ('cols: ',dataset30.RasterXSize, 'rows: ',dataset40.RasterYSize)

    #assign red array  to red array dataset as Read As Array function and convert to float type
    redarray = dataset30.ReadAsArray().astype(float)
    #assign inf red array to inf red array dataset as Read As Array function and convert to float type
    infred = dataset40.ReadAsArray().astype(float)

    #set arrays to empty arrays
    redarray[redarray<0]=0
    infred[infred<0]=0

    
    ndvi_array = numpy.empty([1500,1500])

    #loop through rows
    for row in range(0,1499): #change to (dataset.RasterYSize) if memory is large
        #loop through columns
        for col in range(0,1499): #change to (dataset.RasterXSize) if memory is large
            #perform NDVI calculation 
            ndvi_array[row,col] = (infred[row,col] - redarray[row,col]) / (infred[row,col] + redarray[row,col])
    
    print(ndvi_array)
            #infred[row,col] , redarray[row,col] do calculation on pdf





    #print mean val of ndvi_array
    meanVal = numpy.mean(ndvi_array)
    print ('new meanVal:',meanVal)

    #use geotransform on dataset 30 in order to find its xorigin,yorigin, pixelwidth, and pixel height
    geotransform = dataset30.GetGeoTransform()
    if geotransform:
        xOrigin = geotransform[0]
        yOrigin = geotransform[3]
        pixelWidth = geotransform[1]
        pixelHeight = geotransform[5]
        print ("Origin = ({}, {})", xOrigin, yOrigin)
        print ("Pixel Size = ({}, {})", pixelWidth,pixelHeight)

    rasterOrigin = (505689.75,5003075.25) 
    pixelWidth = 28.5
    pixelHeight = -28.5
    #assign a raster file name
    newRasterFileName = 'gdal_binary.tif'


 #convert numeric array to raster image
    array2raster(newRasterFileName,rasterOrigin,pixelWidth,pixelHeight,ndvi_array)


