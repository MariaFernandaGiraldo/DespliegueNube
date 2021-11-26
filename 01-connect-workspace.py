from azureml.core.authentication import InteractiveLoginAuthentication
from azureml.core import Workspace

interactive_auth = InteractiveLoginAuthentication(tenant_id="99e1e721-7184-498e-8aff-b2ad4e53c1c2")
ws = Workspace.get(name='mlw-esp-udea',
            subscription_id='2f02600d-4773-4737-b32f-643d9d0f66e9',
            resource_group='rg_ml_UDEA',
            location='eastus',
            auth=interactive_auth
            )
ws.write_config(path='.azureml')