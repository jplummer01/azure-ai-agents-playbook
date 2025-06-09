@description('Name of the Logic App workflow')
param workflowName string = 'agent-logic-apps'

@description('Primary location for all resources')
param location string = resourceGroup().location

@description('Tags to apply to resources')
param tags object = {}

@description('Subscription ID for the Outlook connection')
param subscriptionId string

@description('Resource group name for the Outlook connection')
param outlookConnectionResourceGroup string

@description('Name of the Outlook connection')
param outlookConnectionName string = 'outlook'

// Construct the full connection ID
var outlookConnectionId = '/subscriptions/${subscriptionId}/resourceGroups/${outlookConnectionResourceGroup}/providers/Microsoft.Web/connections/${outlookConnectionName}'





resource logicApp 'Microsoft.Logic/workflows@2019-05-01' = {
  name: workflowName
  location: location
  tags: tags
  properties: {
    state: 'Enabled'
    definition: {
      '$schema': 'https://schema.management.azure.com/providers/Microsoft.Logic/schemas/2016-06-01/workflowdefinition.json#'
      contentVersion: '1.0.0.0'
      parameters: {
        '$connections': {
          defaultValue: {}
          type: 'Object'
        }
      }
      triggers: {
        When_a_HTTP_request_is_received: {
          type: 'Request'
          kind: 'Http'
          inputs: {
            schema: {
              type: 'object'
              properties: {
                to: {
                  type: 'string'
                }
                subject: {
                  type: 'string'
                }
                body: {
                  type: 'string'
                }
              }
            }
          }
          description: 'HTTPTrigger'
          operationOptions: 'EnableSchemaValidation'
        }
      }
      actions: {
        'Send_an_email_(V2)': {
          runAfter: {}
          type: 'ApiConnection'
          inputs: {
            host: {
              connection: {
                name: '@parameters(\'$connections\')[\'outlook\'][\'connectionId\']'
              }
            }
            method: 'post'
            body: {
              To: '@triggerBody()?[\'to\']'
              Subject: '@triggerBody()?[\'subject\']'
              Body: '<p class="editor-paragraph">@{triggerBody()?[\'body\']}</p>'
              Importance: 'Normal'
            }
            path: '/v2/Mail'
          }
        }
      }
      outputs: {}
    }
    parameters: {
      '$connections': {
        value: {
          outlook: {
            id: '/subscriptions/${subscriptionId}/providers/Microsoft.Web/locations/${location}/managedApis/outlook'
            connectionId: outlookConnectionId
            connectionName: outlookConnectionName
          }
        }
      }
    }
  }
}

// Output basic information (no secrets)
output workflowName string = logicApp.name
output workflowId string = logicApp.id
output accessEndpoint string = logicApp.properties.accessEndpoint
