##Run on tools-db

use u13367__mostLinkedMissing;
create table if not exists mostLinkedMissingNew ( namespace tinyint(10) , title varchar(256) , value tinyint(10) );
source dump.sql
