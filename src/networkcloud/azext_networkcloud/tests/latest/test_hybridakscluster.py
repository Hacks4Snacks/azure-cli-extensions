# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# --------------------------------------------------------------------------------------------
# pylint: disable=too-few-public-methods,unnecessary-pass,unused-argument

"""
HybridAksCluster test scenarios
"""

from azure.cli.testsdk import ScenarioTest
from azure.cli.testsdk.scenario_tests import AllowLargeResponse
from .config import CONFIG


def setup_scenario1(test):
    ''' Env setup_scenario1 '''


def cleanup_scenario1(test):
    '''Env cleanup_scenario1 '''


def call_scenario1(test):
    ''' # Testcase: scenario1'''
    setup_scenario1(test)
    step_update(test, checks=[
        test.check('tags', '{tagsUpdate}'),
        test.check('provisioningState', 'Succeeded')
    ])
    step_show(test, checks=[])
    step_list_subscription(test)
    step_list_resource_group(test, checks=[])
    cleanup_scenario1(test)


def step_show(test, checks=None):
    '''hybridakscluster show operation'''
    if checks is None:
        checks = []
    test.cmd('az networkcloud hybridakscluster show --name {name} '
             '--resource-group {rg}', checks=checks)


def step_list_resource_group(test, checks=None):
    '''hybridakscluster list by resource group operation'''
    if checks is None:
        checks = []
    test.cmd('az networkcloud hybridakscluster list --resource-group {rg}')


@AllowLargeResponse
def step_list_subscription(test):
    '''hybridakscluster list by subscription operation'''
    test.cmd('az networkcloud hybridakscluster list')


def step_update(test, checks=None):
    '''hybridakscluster update operation'''
    if checks is None:
        checks = []
    test.cmd(
        'az networkcloud hybridakscluster update --name {name} '
        '--tags {tagsUpdate} --resource-group {rg}')


class HybridAksClusterScenarioTest1(ScenarioTest):
    '''hybridakscluster Scenario test'''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.kwargs.update({
            # Autogenerated resource group and name are not used in this scenario because the Hybrid AKS Cluster
            # is created when a tenant creates the provisioned cluster
            'name': CONFIG.get('HYBRID_AKS_CLUSTER', 'name'),
            'rg': CONFIG.get('HYBRID_AKS_CLUSTER', 'resource_group'),
            'tags': CONFIG.get('HYBRID_AKS_CLUSTER', 'tags'),
            'tagsUpdate': CONFIG.get('HYBRID_AKS_CLUSTER', 'tags_update'),
        })

    def test_hybridakscluster_scenario1(self):
        ''' test scenario for hybridakscluster CRUD operations'''
        call_scenario1(self)
