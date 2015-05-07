MySql related queries I don't remember and need often end up googling

==============================================================================
1. Check if a table is view/base table
  
  show full tables in (database)  where Tables_in_(database)="(table_name)";

  E.g., Database => MyDB Table=>mytable

  show full tables in MyDB where Tables_in_MyDB="mytable";

==============================================================================
