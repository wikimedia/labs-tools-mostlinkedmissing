##Run on tools-db

use s53348__mostLinkedMissing;
drop table if exists mostLinkedMissingOld;
create table if not exists mostLinkedMissingNew ( namespace int , title varchar(256) , value int );
create table if not exists mostLinkedMissing ( namespace int , title varchar(256) , value int );
rename table mostLinkedMissing to mostLinkedMissingOld;
rename table mostLinkedMissingNew to mostLinkedMissing;
