# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code originally generated by aaz-dev-tools and facilitates integration of custom code
# --------------------------------------------------------------------------------------------
# pylint: disable=too-many-lines,import-outside-toplevel
# pylint: disable=too-many-statements

''' Load Command model table importing custom commands'''


def load_command_table(self, _):  # pylint: disable=unused-argument
    ''' Custom code imported in this function is loaded via:
     cli-ext/v20221212preview/ext/src/networkcloud/azext_networkcloud/__init__.py
    '''
    # baremetalmachine
    from .operations.baremetalmachine._run_command import RunCommand
    self.command_table["networkcloud baremetalmachine run-command"] = RunCommand(
        loader=self)
    from .operations.baremetalmachine._run_read_command import \
        RunReadCommand
    self.command_table["networkcloud baremetalmachine run-read-command"] = RunReadCommand(
        loader=self)
    from .operations.baremetalmachine._run_data_extract import \
        RunDataExtract
    self.command_table["networkcloud baremetalmachine run-data-extract"] = RunDataExtract(
        loader=self)

    # cluster
    from .operations.cluster.metricsconfiguration._create import \
        ClusterMetricsConfigurationCreate
    self.command_table["networkcloud cluster metricsconfiguration create"] = \
        ClusterMetricsConfigurationCreate(loader=self)

    from .operations.cluster.metricsconfiguration._update import \
        ClusterMetricsConfigurationUpdate
    self.command_table["networkcloud cluster metricsconfiguration update"] = \
        ClusterMetricsConfigurationUpdate(loader=self)

    from .operations.cluster.metricsconfiguration._delete import \
        ClusterMetricsConfigurationDelete
    self.command_table["networkcloud cluster metricsconfiguration delete"] = \
        ClusterMetricsConfigurationDelete(loader=self)

    from .operations.cluster.metricsconfiguration._show import \
        ClusterMetricsConfigurationShow
    self.command_table["networkcloud cluster metricsconfiguration show"] = \
        ClusterMetricsConfigurationShow(loader=self)

    # virtualmachine
    from .operations.virtualmachine._create import VirtualMachineCreate
    self.command_table["networkcloud virtualmachine create"] = VirtualMachineCreate(
        loader=self)
