# Git Commands - Run these after installing Git

# Initialize git repository
git init

# 1. Add backend configuration files
git add backend/.env
git add backend/.gitignore
git add backend/pyproject.toml
git add backend/requirements.txt
git add backend/Makefile
git add backend/README.md
git add backend/conftest.py
git commit -m "feat: add backend configuration files"

# 2. Add Django project structure
git add backend/manage.py
git add backend/config/__init__.py
git add backend/config/asgi.py
git add backend/config/wsgi.py
git add backend/config/urls.py
git add backend/config/settings/__init__.py
git add backend/config/settings/base.py
git add backend/config/settings/dev.py
git add backend/config/settings/prod.py
git commit -m "feat: add Django project configuration"

# 3. Add common app
git add backend/apps/__init__.py
git add backend/apps/common/__init__.py
git add backend/apps/common/admin.py
git add backend/apps/common/apps.py
git add backend/apps/common/models.py
git add backend/apps/common/tests.py
git add backend/apps/common/views.py
git add backend/apps/common/exceptions.py
git add backend/apps/common/pagination.py
git add backend/apps/common/permissions.py
git add backend/apps/common/utils/__init__.py
git add backend/apps/common/utils/helpers.py
git add backend/apps/common/tests/__init__.py
git add backend/apps/common/migrations/__init__.py
git commit -m "feat: add common app with utilities"

# 4. Add users app
git add backend/apps/users/__init__.py
git add backend/apps/users/admin.py
git add backend/apps/users/apps.py
git add backend/apps/users/models.py
git add backend/apps/users/views.py
git add backend/apps/users/urls.py
git add backend/apps/users/serializers.py
git add backend/apps/users/selectors.py
git add backend/apps/users/services.py
git add backend/apps/users/signals.py
git add backend/apps/users/tests.py
git add backend/apps/users/tests/__init__.py
git add backend/apps/users/tests/test_models.py
git add backend/apps/users/migrations/__init__.py
git add backend/apps/users/migrations/0001_initial.py
git commit -m "feat: add users app with custom User model"

# 5. Add Docker files
git add backend/Dockerfile
git add backend/docker-compose.yml
git commit -m "feat: add Docker configuration"

# 6. Add scripts
git add backend/scripts/wait_for_db.py
git add backend/scripts/seed_demo.py
git add backend/scripts/test_api.py
git commit -m "feat: add utility scripts"

# 7. Add requirements
git add backend/requirements/base.txt
git add backend/requirements/dev.txt
git add backend/requirements/prod.txt
git commit -m "feat: add Python requirements"

# 8. Add empty directories with .gitkeep
git add backend/templates/.gitkeep
git add backend/static/.gitkeep
git add backend/media/.gitkeep
git commit -m "feat: add static directories"

# 9. Add frontend structure
git add frontend/src/app/layout.js
git add frontend/src/app/page.js
git add frontend/src/styles/globals.scss
git add frontend/src/styles/variables.scss
git add frontend/src/styles/mixins.scss
git add frontend/package.json
git add frontend/next.config.mjs
git add frontend/jsconfig.json
git add frontend/Dockerfile
git add frontend/docker-compose.yml
git add frontend/.env.local
git add frontend/.gitignore
git commit -m "feat: add Next.js frontend structure"

# 10. Add frontend directories
git add frontend/public/assets/css/.gitkeep
git add frontend/public/assets/fonts/.gitkeep
git add frontend/public/assets/img/.gitkeep
git add frontend/public/assets/scss/.gitkeep
git add frontend/src/common/.gitkeep
git add frontend/src/components/.gitkeep
git add frontend/src/context/.gitkeep
git add frontend/src/data/.gitkeep
git add frontend/src/forms/.gitkeep
git add frontend/src/hooks/.gitkeep
git add frontend/src/layout/.gitkeep
git add frontend/src/modals/.gitkeep
git add frontend/src/plugins/.gitkeep
git add frontend/src/services/.gitkeep
git add frontend/src/svg/.gitkeep
git add frontend/src/ui/.gitkeep
git add frontend/src/utils/.gitkeep
git commit -m "feat: add frontend directory structure"

# 11. Add documentation
git add BACKEND_GUIDE.md
git commit -m "docs: add backend documentation"

# 12. Add root files
git add .gitkeep
git commit -m "chore: add root gitkeep"

# Set main branch
git branch -M main

# Add remote origin
git remote add origin https://github.com/Oshioxi2003/structure.git

# Push to GitHub
git push -u origin main
