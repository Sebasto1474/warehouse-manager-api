### WAREHOUSE MANAGER  API

#### Description
This api works as a simple inventory manager system where users can add, move and remove materials from stock.
All inventory changes are performed through transfers (IN, MOVE, OUT) which are the only way to modify stock levels.

#### Problem statement
The main objective of this API is to provide a simple inventory management tool for small companies that usually track stock using spreadsheets or manual processes.
It centralizes inventory movements and enforces basic business rules to keep stock consistent.

#### Business rules
		Stock levels can only be modified through transfers.
		Transfer types: 
			IN (entry) 
			MOVE (internal movements)
			OUT (take out)
		Only registered users are allowed to perform transfers.
		A material is deleted when its stock reaches zero.

#### Scope
###### Features included
		Create and login as a user.
		Create and delete materials (stock is managed only through transfers)
		Stock movements through transfers.
		A maximum of fifty warehouse positions.
		Transfer history tracking.
		Retrieve material stock by ID.
		Retrieve material locations.
		List all materials with their quantities and locations.
###### Not included
		Managing more than fifty warehouse locations.
		Dynamic creation of new warehouse positions..
		Supplier and customer managment.
		Purchase and sales order managment.

#### Core concepts
###### User
Represent a registered user of the system. Only authenticated users are allowed to perform transfers and manage materials.
Users are responsible for executing inventory operations, providing traceability for stock movements.
###### Material
Represents any item stored in the inventory. A material can only exist if it has stock.
Materials are created through IN transfers and are automatically deleted when their stock reaches zero.
###### Locations
It represents a physical position in the warehouse. Locations are identified by a two-character code:
the first character represents the hallway (A–E), and the second represents the position number (0–9).
The warehouse contains a total of fifty locations. Each location can hold only one material at a time.
Locations can be queried to determine whether they are available or occupied.
###### Transfer
Represents a stock movement and is the only way to modify inventory levels.
There are three types of transfers:
	IN: Adds a material to the inventory. A quantity must be provided. If the material does not exist, it is created.
	OUT: Removes a quantity of a material from the inventory. Stock cannot become negative.
	MOVE: Relocates a material from one location to another. This operation does not modify stock quantity.

All transfers are executed by authenticated users and are stored to provide a complete inventory movement history.
