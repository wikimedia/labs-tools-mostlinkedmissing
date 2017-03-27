##Run on tools-db

use s52741__mostLinkedMissing;
drop table if exists mostLinkedMissingOld;
rename table mostLinkedMissing to mostLinkedMissingOld;
rename table mostLinkedMissingNew to mostLinkedMissing;
