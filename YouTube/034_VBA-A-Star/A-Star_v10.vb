Option Explicit

Public writeScores As Boolean

Public Enum PathColors
    COLOR_EVALUATED = 16751052    ' Light Blue (200, 200, 255)
    COLOR_DISCOVERED = 14481663   ' Light Yellow (255, 255, 200)
    COLOR_FINAL_PATH = 16711680   ' Blue (0, 0, 255)
    COLOR_START = 192             ' Red (Bad style)
    COLOR_GOAL = 3947580          ' Green (Good style)
    COLOR_OBSTACLE = 12632256     ' Gray (Accent1 style)
End Enum

Public Enum distanceMethod
    Heuristic       ' Uses octile distance (diagonal-aware)
    Manhattan       ' Uses Manhattan distance (grid-based)
End Enum

Public Enum cost
    straight = 10       ' Cost for horizontal/vertical movement
    diagonal = 14       ' Cost for diagonal movement (~v2 * 10)
End Enum

Public Enum delay
    znone = 0
    aquicker = 30
    bquick = 100
    ctiny = 300
    dsmall = 400
    ebig = 700
    fhuge = 1000
End Enum

Function PLAYGROUND(Optional newRange As Range) As Range
    Set PLAYGROUND = Range("A1:AN60")
End Function

Sub Main()
    
    Dim openSet As New Collection
    Dim closedSet As New Collection
    Dim gScore As Object, fScore As Object, cameFrom As Object
    
    Set gScore = CreateObject("Scripting.Dictionary")
    Set fScore = CreateObject("Scripting.Dictionary")
    Set cameFrom = CreateObject("Scripting.Dictionary")
    
    ' Initialize start and goal
    Dim start As Range, goal As Range
    Set start = LocateMarker(PLAYGROUND, "s")
    If start Is Nothing Then Set start = PLAYGROUND.Cells(1, 1)
    
    Set goal = LocateMarker(PLAYGROUND, "g")
    If goal Is Nothing Then Set goal = PLAYGROUND.Cells(PLAYGROUND.Rows.Count, PLAYGROUND.Columns.Count)
    Dim myDistanceMethod As distanceMethod
    
    'User input start
    myDistanceMethod = distanceMethod.Manhattan
    writeScores = False
    'PLAYGROUND could be set as well
    'Play with the diagonal and straight costs, if you wish
    'User input end
    
    start.Style = "Bad"
    goal.Style = "Good"
    FixFontSize
    
    ' Initialize scores
    openSet.Add start
    gScore(start.Address) = 0
    fScore(start.Address) = DistanceCalculator(start, goal, myDistanceMethod)
    
    ' Main A* loop
    Dim current As Range, neighbor As Range
    Dim i As Long, j As Long, tempG As Long, inOpen As Boolean, pathFound As Boolean
    Dim moveCost As Long
    
    Do While openSet.Count > 0
        ' Get node with lowest fScore
        Set current = GetLowestFScoreNode(openSet, fScore)
        
        ' Check if goal reached
        If current.Address = goal.Address Then
            pathFound = True
            Exit Do
        End If
        
        ' Move current to closed set
        RemoveFromCollection openSet, current
        closedSet.Add current
        ColorCell current, COLOR_EVALUATED, start, goal, gScore, fScore
        
        ' Check all 8 neighbors
        For i = -1 To 1
            For j = -1 To 1
                If Not (i = 0 And j = 0) Then
                    If current.Row + i >= 1 And current.Row + i <= PLAYGROUND.Rows.Count And _
                       current.Column + j >= 1 And current.Column + j <= PLAYGROUND.Columns.Count Then
                        
                        Set neighbor = current.Offset(i, j)
                        
                        If IsValidNeighbor(current, neighbor, i, j, closedSet, goal) Then
                            moveCost = IIf((i <> 0 And j <> 0), cost.diagonal, cost.straight)
                            tempG = gScore(current.Address) + moveCost
                            inOpen = InCollection(openSet, neighbor)
                            
                            ' Update path if better
                            If Not inOpen Or tempG < gScore(neighbor.Address) Then
                                cameFrom(neighbor.Address) = current.Address
                                gScore(neighbor.Address) = tempG
                                fScore(neighbor.Address) = tempG + DistanceCalculator(neighbor, goal, myDistanceMethod)
                                
                                If Not inOpen Then
                                    openSet.Add neighbor
                                    ColorCell neighbor, COLOR_DISCOVERED, start, goal, gScore, fScore
                                End If
                            End If
                        End If
                    End If
                End If
            Next j
        Next i
    Loop
    
    ' Backtrack to draw path
    If pathFound Then
        Do While cameFrom.Exists(current.Address)
            Set current = Range(cameFrom(current.Address))
            If Not current.Address = start.Address Then
                current.Interior.color = COLOR_FINAL_PATH
                Wait delay.bquick
            End If
        Loop
        Debug.Print "Path found! Cost: " & gScore(goal.Address)
    Else
        Debug.Print "No path exists."
    End If
End Sub

Private Function IsValidNeighbor(ByRef current As Range, ByRef neighbor As Range, i As Long, j As Long, _
    ByRef closedSet As Collection, ByRef goal As Range) As Boolean
    
    If neighbor.Row < 1 Or neighbor.Row > PLAYGROUND.Rows.Count Or _
       neighbor.Column < 1 Or neighbor.Column > PLAYGROUND.Columns.Count Then
        Exit Function
    End If
    
    ' Skip obstacles and closed nodes
    If neighbor.Interior.color = COLOR_OBSTACLE Or InCollection(closedSet, neighbor) Then
        Exit Function
    End If

    ' Diagonal movement check
    Dim isDiagonal As Boolean
    isDiagonal = (i <> 0 And j <> 0)
    
    If isDiagonal Then
        ' Allow if moving toward goal
        Dim towardGoal As Boolean
        towardGoal = (Sgn(goal.Row - current.Row) = i) And _
                     (Sgn(goal.Column - current.Column) = j)
        
        If Not towardGoal Then
            ' Block only if BOTH adjacent cells are obstacles
            If (current.Offset(i, 0).Interior.color = COLOR_OBSTACLE) And _
               (current.Offset(0, j).Interior.color = COLOR_OBSTACLE) Then
                Exit Function
            End If
        End If
    End If
    
    IsValidNeighbor = True
End Function

Private Function GetLowestFScoreNode(ByRef openSet As Collection, ByRef fScore As Object) As Range
    Dim lowestNode As Range
    Set lowestNode = openSet(1)
    
    Dim node As Range
    For Each node In openSet
        If fScore(node.Address) < fScore(lowestNode.Address) Then
            Set lowestNode = node
        End If
    Next node
    
    Set GetLowestFScoreNode = lowestNode
    
End Function

Private Sub ColorCell(myCell As Range, color As PathColors, start As Range, goal As Range, _
                            ByRef gScore As Object, _
                            ByRef fScore As Object)
                            
    If Not myCell.Address = start.Address And Not myCell.Address = goal.Address Then
        myCell.Interior.color = color
        If writeScores Then
            myCell.Value = gScore(myCell.Address) & "/" & fScore(myCell.Address)
        End If
        
        Wait delay.znone
    End If
    
End Sub

Function DistanceCalculator(cellA As Range, cellB As Range, myDistanceMethod As distanceMethod) As Long
    If myDistanceMethod = Heuristic Then
        DistanceCalculator = HeuristicDistance(cellA, cellB)
    Else
        DistanceCalculator = ManhattanDistance(cellA, cellB)
    End If
End Function

Function HeuristicDistance(cellA As Range, cellB As Range) As Long
    Dim dx As Long: dx = Abs(cellA.Column - cellB.Column)
    Dim dy As Long: dy = Abs(cellA.Row - cellB.Row)
    HeuristicDistance = cost.straight * (dx + dy) + (cost.diagonal - 2 * cost.straight) * Application.WorksheetFunction.Min(dx, dy)
End Function

Function ManhattanDistance(cellA As Range, cellB As Range) As Long
    ManhattanDistance = cost.straight * (Abs(cellA.Row - cellB.Row) + Abs(cellA.Column - cellB.Column))
End Function

Function LocateMarker(searchRange As Range, marker As String) As Range
    Dim myCell As Range
    For Each myCell In searchRange
        If UCase(myCell.Value) = UCase(marker) Then
            Set LocateMarker = myCell
            Exit Function
        End If
    Next myCell
End Function

Function InCollection(col As Collection, item As Range) As Boolean
    Dim element As Range
    For Each element In col
        If element.Address = item.Address Then
            InCollection = True
            Exit Function
        End If
    Next element
End Function

Sub RemoveFromCollection(col As Collection, item As Range)
    Dim i As Long
    For i = 1 To col.Count
        If col(i).Address = item.Address Then
            col.Remove i
            Exit Sub
        End If
    Next i
End Sub

Sub Wait(milliseconds As delay)
    Dim startTime As Double
    startTime = Timer
    Do While Timer < startTime + (milliseconds / 1000)
        DoEvents
    Loop
End Sub

Sub FixFontSize()
    With PLAYGROUND
        .Font.Size = 7
    End With
End Sub

Public Sub ResetAndKeep()
  
    ' Store existing obstacles
    Dim obstacles As Range
    Dim myCell As Range
    
    ' Find all Accent1 cells in playground
    For Each myCell In PLAYGROUND
        If myCell.Interior.color = COLOR_OBSTACLE Then
            If obstacles Is Nothing Then
                Set obstacles = myCell
            Else
                Set obstacles = Union(obstacles, myCell)
            End If
        End If
    Next myCell
    
    If Not obstacles Is Nothing Then
        obstacles.Select
    End If
    
    Reset
    
End Sub

Public Sub Reset()
    
    Cells.Delete
    With PLAYGROUND
        .Style = "Neutral"
        .RowHeight = 14
        .ColumnWidth = 2.3
        .WrapText = True
    End With
    
    FixFontSize
    MakeProblems
        
    PLAYGROUND.Select
    ActiveWindow.Zoom = True
    Cells(1, 1).Select
    
End Sub

Sub MakeProblems()
    Selection.Interior.color = COLOR_OBSTACLE
End Sub

Public Sub Reset1()
    Range("$AH$7,$BA$19:$BH$19,$AT$9:$AT$17,$U$7:$AG$7,$T$7:$T$14,$I$6:$I$15,$M$8:$M$19,$A$4:$A$11,$C$3:$J$3,$D$1:$D$2,$AU$4:$BF$4,$AY$11:$AY$20,$AY$10:$BF$10").Select
    Reset
End Sub

Public Sub Reset2()
    Range("$G$19:$G$20,$AH$7,$BA$19:$BH$19,$AT$9:$AT$17,$U$7:$AG$7,$T$7:$T$14,$I$6:$I$15,$M$8:$M$19,$A$4:$A$11,$C$3:$J$3,$D$1:$D$16,$AU$4:$BF$4,$AY$11:$AY$20,$AY$10:$BF$10,$BC$14:$BH$14,$AV$7:$BF$7,$AL$3:$AL$20,$AI$1:$AI$18,$AA$10:$AA$20,$AC$3:$AC$14,$P$5:$P$20").Select
    Reset
End Sub

