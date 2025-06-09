targetScope = 'subscription'

@minLength(1)
@maxLength(64)
@description('Name of the environment that can be used as part of naming resource convention')
param environmentName string

@minLength(1)
@description('Primary location for all resources')
param location string

@minLength(1)
@maxLength(32)
@description('Name of the resource group')
param rgName string


@description('Subscription ID for the Outlook connection')
param outlookConnectionSubscriptionId string = subscription().subscriptionId

@description('Resource group name for the Outlook connection')
param outlookConnectionResourceGroup string

@description('Name of the Outlook connection')
param outlookConnectionName string = 'outlook'

resource resourceGroup 'Microsoft.Resources/resourceGroups@2021-04-01' = {
  name: '${abbrs.resourcesResourceGroup}-${rgName}'
  location: location
  tags: tags
}

var resourceGroupName = resourceGroup.name
var randomSuffix = uniqueString(subscription().id, resourceGroupName, environmentName)


var uniqueId = uniqueString(resourceGroup.id)

var tags = {
  'azd-env-name': environmentName
}

var abbrs = {
  resourcesResourceGroup: 'rg'
  logicApp: 'logic'
}


module uami 'modules/uami.bicep' = {
  name: 'uami'
  scope: resourceGroup
  params: {
    uniqueId: uniqueId
    prefix: 'afa-${randomSuffix}-'
    location: location
  }
}

module logicApps 'modules/logic-apps.bicep' = {
  name: 'logic-apps'
  scope: resourceGroup
  params: {
    workflowName: '${abbrs.logicApp}-${environmentName}-${randomSuffix}'
    location: location
    tags: tags
    subscriptionId: outlookConnectionSubscriptionId
    outlookConnectionResourceGroup: outlookConnectionResourceGroup
    outlookConnectionName: outlookConnectionName
  }
}

output AZURE_LOCATION string = location
output LOGIC_APP_NAME string = logicApps.outputs.workflowName
output LOGIC_APP_ID string = logicApps.outputs.workflowId
output LOGIC_APP_ENDPOINT string = logicApps.outputs.accessEndpoint
