Option Explicit

' http://www.vitoshacademy.com/run-python-funct…m-excel-with-vba/
' Library - Microsoft Scripting Runtime

Sub TestMe()
    Dim path As String: path = "C:\Python\"
    Dim pathExe As String
    Dim i As Long
    Dim txtStream As TextStream
    Dim fso As New FileSystemObject
    Dim fileName As String
    
    Columns("C:D").Clear
    For i = 1 To 8
    
        fileName = "file" & i & ".txt"
        pathExe = path & "CodeForces.py" & " """ & Cells(i, 1) & """ >" & path & fileName
        Shell "cmd.exe /S /c " & pathExe
        
        Application.Wait Now + #12:00:01 AM#
        Set txtStream = fso.OpenTextFile(path & fileName)
        Cells(i, 3) = txtStream.ReadLine
        txtStream.Close
        'Kill path & fileName
        
        If Cells(i, 3) = Cells(i, 2) Then Cells(i, 4) = "Pass..."
                
    Next i

End Sub



