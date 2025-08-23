# Docker Basics in Excel with VBA | Full CRUD Demo

## YouTube video

## VitoshAcademy blog

* `SeedTodos()` - quickly inserts a few sample todos into the API, so we don’t start from an empty sheet.
* `ListTodosToSheet()` - pulls all todos into Sheet1. It writes ID, Title, and Completed columns, so you can see the live state.
* `DumpTodosToImmediate()` - prints the same list into the VBA Immediate Window (Ctrl+G). Handy for quick debugging.
* `?CreateTodo("Watch VitoshAcademy", True)` - creates a new todo with a title and completed flag. The ? in the Immediate Window prints the returned ID.
* `UpdateTodoTitle 1, "Watch VitoshAcademy"` - updates the title of the todo with ID=1.
* `SetTodoCompleted 1, True` - marks the same item as completed.
* `GetTodoById 1` - fetches a single item as raw JSON, displayed in the Immediate Window.
* `DeleteTodo 1` - removes the todo with ID=1.
* `DeleteAllTodos()` - wipes everything in the list (careful with this one :)).
* `ListTodosToSheet()` - refresh the sheet after changes to confirm results.
* `PushSheetToApi()` - the powerful one: reads rows from Excel (ID, Title, Completed, Action) and syncs them back to the API. That way you can create, update, or delete tasks directly from the sheet.