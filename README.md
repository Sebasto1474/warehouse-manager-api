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
