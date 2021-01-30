# Pettify makefile

MANAGE=python manage.py

help: ## Display the help
	@echo "Pettify backend makefile directives:\n"
	@grep '\#\#' Makefile | sed -e 's/\#\#/->/g'
	@echo ""

up: ## Start the development server
	$(MANAGE) runserver localhost:8000

db: ## Recreate the database
	$(MANAGE) reset_db --noinput
	$(MANAGE) makemigrations pettify_crm
	$(MANAGE) migrate
	$(MANAGE) loaddata ./pettify_crm/fixtures/*.json

