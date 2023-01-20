# Create a new migration
migration-new:
ifeq ($(strip ${MIGRATION_NEW_ARGS}),)
	@echo "\e[1;31mERROR: A name of migration is required\e[0m"
else
	@dbmate ${DBMATE_OPTIONS} new ${MIGRATION_NEW_ARGS}
endif

# Create the database (if it does not already exist) and run any pending migrations
migration-up:
	@dbmate ${DBMATE_OPTIONS} up

# Roll back the most recent migration
migration-down:
	@dbmate ${DBMATE_OPTIONS} rollback

# Show the status of all migrations
migration-status:
	@dbmate ${DBMATE_OPTIONS} status