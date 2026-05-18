
#import glad,ogr, sys, numpy, and math, 
from osgeo import gdal,ogr
import sys
import numpy
import math



#Assign file name to Powerline file 
filename = 'PowerLine.shp'

#Assign file name to Parcels file 
filename2 = 'Parcels.shp'

driver = ogr.GetDriverByName('ESRI Shapefile')

#get driver appropriate for input file for part 2 of assignment
driver2 = ogr.GetDriverByName('ESRI Shapefile')

#step 2 --- open the file using the driver
dataSource = driver.Open(filename, gdal.GA_ReadOnly)

#open the file using the driver2 for part 2 of assignment
dataSource2 = driver2.Open(filename2, gdal.GA_ReadOnly)

#verify the file was opened, exit if not opened
if dataSource is None:
    print('Failed to open file')
    sys.exit(1)

#verify the second file was opened, exit if not opened for part 2 of assignment
if dataSource2 is None:
    print('Failed to open file')
    sys.exit(1)



layer        = dataSource.GetLayer(0)

#get the first (and only) data layer for part 2 of assignment
layer2        = dataSource2.GetLayer(0)

#get basic info about the layer
layerName    = layer.GetName()
layerTypeInt = layer.GetGeomType()
layerExtent  = layer.GetExtent()

#get basic info about the layer for part 2 of assignment
layerName2    = layer2.GetName()
layerTypeInt2 = layer2.GetGeomType()
layerExtent2  = layer2.GetExtent()

#convert integer layertype to text equivalent
layerTypeStr = ogr.GeometryTypeToName(layerTypeInt)


#convert integer layertype to text equivalent for part 2 of assignment
layerTypeStr2 = ogr.GeometryTypeToName(layerTypeInt2)

#print the name, type and extent of layer
print('Layer', layerName,'is a', layerTypeStr,'layer with bounding box:')
print(layerExtent,'\n')

#print the name, type and extent of layer for part 2 of assignment
print('Parcel Layer', layerName2,'is a', layerTypeStr2,'layer with bounding box:')
print(layerExtent2,'\n')

#step 4a get access to the layer's non-spatial info: number of fields, field names, field types, etc.
featureDefn = layer.GetLayerDefn()

#get access to the layer's non-spatial info: number of fields, field names, field types, etc. for part 2 of assignment
featureDefn2 = layer2.GetLayerDefn()

#get and print the number of fields
fieldCount = featureDefn.GetFieldCount()
#print("The layer's feature definition has the following", fieldCount, "fields:")


#get and print the number of fields for part 2 of assignment
fieldCount2 = featureDefn2.GetFieldCount()
#print("The Parcel layer's feature definition has the following", fieldCount2, "fields:")

#step 4b print info about every field
for i in range(0,fieldCount):
    fieldDef    = featureDefn.GetFieldDefn(i)
    fname       = fieldDef.GetNameRef()
    fwidth      = fieldDef.GetWidth()
    fprecision  = fieldDef.GetPrecision()
    ftype       = fieldDef.GetType()
    ftypeS = fieldDef.GetFieldTypeName(ftype)#convert integer ftype to text equiv
    values = (fname,ftypeS,fwidth,fprecision)
    #print(values)


#Part 1: Calculate length of power line in miles for Powerline file

#step 5 get info about each feature
featureCount = layer.GetFeatureCount()
#print('There are',featureCount,'features:')
for i in range(featureCount):
    feature = layer.GetFeature(i)

    #step 5b --- get the feature’s geometry
    geometry = feature.GetGeometryRef()
    
    nPts = geometry.GetPointCount()
    #print(nPts)  #access points index 0-3
    total=0 #assign total to 0 to calculate total of points later
    for i in range(nPts-1):
        #assign point 1 to point1 variable
        point1 = geometry.GetPoint(i)
        #assign point 2 to point 2 variable
        point2 = geometry.GetPoint(i+1)
        #perform calculation to calculate length between points
        calc = math.sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)
        #add each calculation to the total
        total = (total + calc)
        #Convert to miles
        final = total / 5280
        #Round to two decimal places
        final2 = round(final,2)
    #print the distance
    print('The line length of the Power Line figure is:',final2,'miles')
        

print("The Parcel layer's feature definition has the following", fieldCount2, "fields:")
for i in range(0,fieldCount2):
    fieldDef2    = featureDefn2.GetFieldDefn(i)
    fname2       = fieldDef2.GetNameRef()
    fwidth2      = fieldDef2.GetWidth()
    fprecision2  = fieldDef2.GetPrecision()
    ftype2       = fieldDef2.GetType()
    ftypeS2 = fieldDef2.GetFieldTypeName(ftype2)#convert integer ftype to text equiv
    values2 = (fname2,ftypeS2)
    print(values2)

    
featureCount2 = layer2.GetFeatureCount()
#print('There are',featureCount2,'features:')
print('The following addresses and areas of every parcel are ones that are crossed by the power line:')
for i in range(featureCount2):
    feature2 = layer2.GetFeature(i)
    geometry2 = feature2.GetGeometryRef()
    #get address
    address = feature2.GetField('SITUSADDR')
    #get area
    area = feature2.GetField('AREA')
    if geometry.Crosses(geometry2):
        #if lines cross print address and area
        finalprint = (address,area)
        print(finalprint)
    
    

dataSource = None

dataSource2 = None

