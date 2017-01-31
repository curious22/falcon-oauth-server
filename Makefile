ENV_ROOT=.venv/
PYBINARYDIR=$(ENV_ROOT)bin/
PYTHON=$(PYBINARYDIR)python

start-server:
	@echo '----- Start a gunicorn server -----'
	$(PYTHON) $(PYBINARYDIR)gunicorn -b 0.0.0.0:5000 --reload app.main:application
