#!/bin/bash

#Update data on replica
sql cswiki < updateReplica.sql
#Copy them to a temp file
mysqldump -h cswiki.labsdb u13367__mostLinkedMissing mostLinkedMissingNew > dump.sql
#Copy them to tools-db
sql local < toLocal.sql
#Rm the temp file
rm dump.sql
#Cleanup
sql cswiki < cleanUp.sql
