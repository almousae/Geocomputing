from osgeo import gdal
from osgeo import osr
import numpy

#create a function 
def array2raster(newRasterFileName,rasterOrigin,pixelWidth,pixelHeight,array):
     #Step 1-- choose a driver
     outformat = 'GTiff'
     outDriver = gdal.GetDriverByName(outformat) 

     #Step 2 -- Create output dataset using that driver
     rows  = array.shape[0] 
     cols    = array.shape[1]
     print ('rows: ', rows, ' cols: ', cols)
     nBands   = 1
     dataType = gdal.GDT_Float32
     dsOut=outDriver.Create(newRasterFileName,cols,rows,nBands,dataType)

     #Step 3 -- Set Geotransform
     xCorner=rasterOrigin[0]
     yCorner=rasterOrigin[1]
     xOffset=0
     yOffset=0 
     geoT = [ xCorner, pixelWidth, xOffset, yCorner, yOffset, -pixelHeight]
     dsOut.SetGeoTransform( geoT )

     #Step 4 -- Set Projection
     mySrs = osr.SpatialReference()
     #mySrs.SetWellKnownGeogCS("WGS84")
     mySrs.ImportFromEPSG(4326) #WGS84 http://spatialreference.org/ref/epsg/
     myWKT = mySrs.ExportToWkt()
     #print myWKT
     dsOut.SetProjection(myWKT)

     #Step 5 -- Process Each Band 
     outband = dsOut.GetRasterBand(1)
     outband.SetColorInterpretation(gdal.GCI_Undefined)
     outband.WriteArray(array)
     outband.FlushCache()

     #Step 6 -- Close the output data 
     dsOut=None

## the main function
if __name__ == "__main__":
    rasterOrigin = (-89.40089,43.07585) #any geographic coordinate in WGS 1984
    pixelWidth = 10
    pixelHeight = 10
    newRasterFileName = 'gdal_binary.tif'
    array = numpy.array([[ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                      [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                      [ 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1],
                      [ 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
                      [ 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1],
                      [ 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
                      [ 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
                      [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                      [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                      [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])
    #convert numeric array to raster image
    array2raster(newRasterFileName,rasterOrigin,pixelWidth,pixelHeight,array)
    
