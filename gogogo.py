import vtk
import json
import os

# 首先设定输入的文件名
fileName = 'st'

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    reader = vtk.vtkPolyDataReader()

    reader.SetFileName('inputVTKfile/'+fileName + '.vtk')  # SetFileName设置要读取的vtk文件
    reader.ReadAllScalarsOn()
    reader.ReadAllVectorsOn()
    reader.ReadAllTensorsOn()
    reader.Update()

    vtkdata = reader.GetOutput()  # GetOutput获取文件的数据

    # 处理scalar
    scalars = vtkdata.GetPointData().GetScalars('scalars')
    length = scalars.GetNumberOfValues()
    result = []
    for i in range(length):
        result.append(scalars.GetValue(i))
    if not os.path.exists('./' + fileName):
        os.mkdir('./' + fileName)
    with open('./' + fileName + '/scalars.json', 'w') as file_obj:
        json.dump(result, file_obj)

    # 处理points
    points = vtkdata.GetPoints().GetData()
    length = points.GetNumberOfValues()
    result = []
    for i in range(length):
        result.append(points.GetValue(i))
    with open('./' + fileName + '/points.json', 'w') as file_obj:
        json.dump(result, file_obj)

    # 处理lines
    lines = vtkdata.GetLines().GetData()
    length = lines.GetNumberOfValues()
    result = []
    for i in range(length):
        result.append(lines.GetValue(i))
    print(len(result), length)
    with open('./' + fileName + '/lines.json', 'w') as file_obj:
        json.dump(result, file_obj)
