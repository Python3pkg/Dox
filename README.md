Dox
===

Markdown-oriented content authoring for Axilent.

Basic Idea
----

Initialization

	cd mydocs
	dox init
	"Enter Axilent Library Key"
	187fee27efc843ed88d7b32b0f706811
	"Enter Axilent Project"
	myproject
	"Enter content type"
	Article
	"Enter name of body field."
	body
	"Dox Initialized"
	
Post Content

	touch "Hello World" > hello.md
	dox upload
	"Uploading..."
	"Added hello.md"
	"Done."

Update Content
	
	touch "Yo, whazzzup" > hello.md
	dox upload
	"Uploading..."
	"Updating hello.md"
	"Done"
	
Deleting Content
	
	rm hello.md
	dox upload
	"Uploading..."
	"Archiving hello.md"
	"Done"
	
