# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "networkfabric fabric create",
)
class Create(AAZCommand):
    """Create a Network Fabric resource.

    :example: Create a Network Fabric with option B Properties
        az networkfabric fabric create --resource-group "example-rg" --location "westus3" --resource-name "example-fabric" --nf-sku "fab1" --nfc-id "/subscriptions/xxxxx-xxxx-xxxx-xxxx-xxxxx/resourceGroups/example-rg/providers/Microsoft.ManagedNetworkFabric/networkFabricControllers/example-NFC" --fabric-asn 20 --ipv4-prefix 10.1.0.0/19 --rack-count 3 --server-count-per-rack 7 --ts-config "{primaryIpv4Prefix:'172.31.0.0/30',secondaryIpv4Prefix:'172.31.0.20/30',username:'****',password:'*****',serialNumber:'1234'}" --managed-network-config "{infrastructureVpnConfiguration:{peeringOption:OptionB,optionBProperties:{importRouteTargets:['65541:2001','65542:2001'],exportRouteTargets:['65531:1002','65531:1002']}},workloadVpnConfiguration:{peeringOption:OptionB,optionBProperties:{importRouteTargets:['65541:2001','65542:2001'],exportRouteTargets:['65531:1002','65531:1002']}}}"

    :example: Create a Network Fabric with option A Properties
        az networkfabric fabric create --resource-group "example-rg" --location "westus3" --resource-name "example-fabric" --nf-sku "fab1" --nfc-id "/subscriptions/xxxxx-xxxx-xxxx-xxxx-xxxxx/resourceGroups/example-rg/providers/Microsoft.ManagedNetworkFabric/networkFabricControllers/example-NFC" --fabric-asn 20 --ipv4-prefix "10.1.0.0/19" --rack-count 3 --server-count-per-rack 7 --ts-config "{primaryIpv4Prefix:'172.31.0.0/30',secondaryIpv4Prefix:'172.31.0.20/30',username:'****',password:'*****',serialNumber:1234}" --managed-network-config "{infrastructureVpnConfiguration:{peeringOption:OptionA,optionAProperties:{mtu:1500,vlanId:520,peerASN:65133,primaryIpv4Prefix:'172.31.0.0/31',secondaryIpv4Prefix:'172.31.0.20/31'}},workloadVpnConfiguration:{peeringOption:OptionA,optionAProperties:{mtu:1500,vlanId:520,peerASN:65133,primaryIpv4Prefix:'172.31.0.0/31',secondaryIpv4Prefix:'172.31.0.20/31'}}}"

    :example: Help text for sub parameters under the specific parent can be viewed by using the shorthand syntax '??'. See https://github.com/Azure/azure-cli/tree/dev/doc/shorthand_syntax.md for more about shorthand syntax.
        az networkfabric fabric create --ts-config ??
        az networkfabric fabric create --managed-network-config "{infrastructureVpnConfiguration:??"
        az networkfabric fabric create --managed-network-config "{infrastructureVpnConfiguration:{option-b-properties:??"
    """

    _aaz_info = {
        "version": "2023-02-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.managednetworkfabric/networkfabrics/{}", "2023-02-01-preview"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_name = AAZStrArg(
            options=["--resource-name"],
            help="Name of the Network Fabric",
            required=True,
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            help="Name of the resource group",
            required=True,
        )

        # define Arg Group "Body"

        _args_schema = cls._args_schema
        _args_schema.location = AAZResourceLocationArg(
            arg_group="Body",
            help="Location of Azure region",
            required=True,
            fmt=AAZResourceLocationArgFormat(
                resource_group_arg="resource_group",
            ),
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Body",
            help="Resource tags.",
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg()

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.annotation = AAZStrArg(
            options=["--annotation"],
            arg_group="Properties",
            help="Switch configuration description.",
        )
        _args_schema.fabric_asn = AAZIntArg(
            options=["--fabric-asn"],
            arg_group="Properties",
            help="ASN of CE devices for CE/PE connectivity. The value should be between 1 to 65535. Example : 65123",
            fmt=AAZIntArgFormat(
                maximum=65535,
                minimum=1,
            ),
        )
        _args_schema.ipv4_prefix = AAZStrArg(
            options=["--ipv4-prefix"],
            arg_group="Properties",
            help="IPv4Prefix for Management Network. Example : 10.1.0.0/19.",
        )
        _args_schema.ipv6_prefix = AAZStrArg(
            options=["--ipv6-prefix"],
            arg_group="Properties",
            help="IPv6Prefix for Management Network. Example : 3FFE:FFFF:0:CD40::/59.",
        )
        _args_schema.managed_network_config = AAZObjectArg(
            options=["--managed-network-config"],
            arg_group="Properties",
            help="Configuration to be used to setup the management network.",
        )
        _args_schema.nfc_id = AAZStrArg(
            options=["--nfc-id"],
            arg_group="Properties",
            help="Network Fabric Controller ARM resource id",
        )
        _args_schema.nf_sku = AAZStrArg(
            options=["--nf-sku"],
            arg_group="Properties",
            help="Fabric SKU id based on the SKU of the BoM that was ordered",
        )
        _args_schema.rack_count = AAZIntArg(
            options=["--rack-count"],
            arg_group="Properties",
            help="Number of racks associated to Network Fabric.Possible values are from 2-8.",
            fmt=AAZIntArgFormat(
                maximum=8,
                minimum=2,
            ),
        )
        _args_schema.server_count_per_rack = AAZIntArg(
            options=["--server-count-per-rack"],
            arg_group="Properties",
            help="Number of servers.Possible values are from 1-16.",
            fmt=AAZIntArgFormat(
                maximum=16,
                minimum=1,
            ),
        )
        _args_schema.ts_config = AAZObjectArg(
            options=["--ts-config"],
            arg_group="Properties",
            help="Network and credentials configuration currently applied to terminal server.",
        )

        managed_network_config = cls._args_schema.managed_network_config
        managed_network_config.infrastructure_vpn_configuration = AAZObjectArg(
            options=["infrastructure-vpn-configuration"],
            help="Configuration for infrastructure vpn.",
            required=True,
        )
        managed_network_config.workload_vpn_configuration = AAZObjectArg(
            options=["workload-vpn-configuration"],
            help="Configuration for workload vpn.",
            required=True,
        )

        infrastructure_vpn_configuration = cls._args_schema.managed_network_config.infrastructure_vpn_configuration
        infrastructure_vpn_configuration.option_a_properties = AAZObjectArg(
            options=["option-a-properties"],
            help="Peering option A properties.",
        )
        cls._build_args_option_a_properties_create(infrastructure_vpn_configuration.option_a_properties)
        infrastructure_vpn_configuration.option_b_properties = AAZObjectArg(
            options=["option-b-properties"],
            help="Option B configuration to be used for management vpn.",
        )
        cls._build_args_option_b_properties_create(infrastructure_vpn_configuration.option_b_properties)
        infrastructure_vpn_configuration.peering_option = AAZStrArg(
            options=["peering-option"],
            help="Peering option list.",
            required=True,
            enum={"OptionA": "OptionA", "OptionB": "OptionB"},
        )

        workload_vpn_configuration = cls._args_schema.managed_network_config.workload_vpn_configuration
        workload_vpn_configuration.option_a_properties = AAZObjectArg(
            options=["option-a-properties"],
            help="Peering option A properties.",
        )
        cls._build_args_option_a_properties_create(workload_vpn_configuration.option_a_properties)
        workload_vpn_configuration.option_b_properties = AAZObjectArg(
            options=["option-b-properties"],
            help="Option B configuration to be used for management vpn.",
        )
        cls._build_args_option_b_properties_create(workload_vpn_configuration.option_b_properties)
        workload_vpn_configuration.peering_option = AAZStrArg(
            options=["peering-option"],
            help="Peering option list.",
            required=True,
            enum={"OptionA": "OptionA", "OptionB": "OptionB"},
        )

        ts_config = cls._args_schema.ts_config
        ts_config.password = AAZStrArg(
            options=["password"],
            help="Password of terminal server.",
            required=True,
        )
        ts_config.primary_ipv4_prefix = AAZStrArg(
            options=["primary-ipv4-prefix"],
            help="IPv4 Address Prefix of CE-PE interconnect links. Example : 172.31.0.0/31.",
            required=True,
        )
        ts_config.primary_ipv6_prefix = AAZStrArg(
            options=["primary-ipv6-prefix"],
            help="IPv6 Address Prefix of CE-PE interconnect links. Example : 3FFE:FFFF:0:CD30::a0/126.",
        )
        ts_config.secondary_ipv4_prefix = AAZStrArg(
            options=["secondary-ipv4-prefix"],
            help="Secondary IPv4 Address Prefix of CE-PE interconnect links. Example : 172.31.0.20/31.",
            required=True,
        )
        ts_config.secondary_ipv6_prefix = AAZStrArg(
            options=["secondary-ipv6-prefix"],
            help="Secondary IPv6 Address Prefix of CE-PE interconnect links. Example : 3FFE:FFFF:0:CD30::a4/126.",
        )
        ts_config.serial_number = AAZStrArg(
            options=["serial-number"],
            help="Serial Number of Terminal server.",
        )
        ts_config.username = AAZStrArg(
            options=["username"],
            help="Username of terminal server.",
            required=True,
        )
        return cls._args_schema

    _args_option_a_properties_create = None

    @classmethod
    def _build_args_option_a_properties_create(cls, _schema):
        if cls._args_option_a_properties_create is not None:
            _schema.mtu = cls._args_option_a_properties_create.mtu
            _schema.peer_asn = cls._args_option_a_properties_create.peer_asn
            _schema.primary_ipv4_prefix = cls._args_option_a_properties_create.primary_ipv4_prefix
            _schema.primary_ipv6_prefix = cls._args_option_a_properties_create.primary_ipv6_prefix
            _schema.secondary_ipv4_prefix = cls._args_option_a_properties_create.secondary_ipv4_prefix
            _schema.secondary_ipv6_prefix = cls._args_option_a_properties_create.secondary_ipv6_prefix
            _schema.vlan_id = cls._args_option_a_properties_create.vlan_id
            return

        cls._args_option_a_properties_create = AAZObjectArg()

        option_a_properties_create = cls._args_option_a_properties_create
        option_a_properties_create.mtu = AAZIntArg(
            options=["mtu"],
            help="MTU to use for option A peering. The value should be between 1500 to 9000. Default value is 1500.",
            fmt=AAZIntArgFormat(
                maximum=9000,
                minimum=1500,
            ),
        )
        option_a_properties_create.peer_asn = AAZIntArg(
            options=["peer-asn"],
            help="Peer ASN number. The value should be between 1 to 65535. Example : 28.",
            fmt=AAZIntArgFormat(
                maximum=65535,
                minimum=1,
            ),
        )
        option_a_properties_create.primary_ipv4_prefix = AAZStrArg(
            options=["primary-ipv4-prefix"],
            help="IPv4 Address Prefix of CE-PE interconnect links. Example : 172.31.0.0/31.",
        )
        option_a_properties_create.primary_ipv6_prefix = AAZStrArg(
            options=["primary-ipv6-prefix"],
            help="IPv6 Address Prefix of CE-PE interconnect links. Example : 3FFE:FFFF:0:CD30::a0/126.",
        )
        option_a_properties_create.secondary_ipv4_prefix = AAZStrArg(
            options=["secondary-ipv4-prefix"],
            help="Secondary IPv4 Address Prefix of CE-PE interconnect links. Example : 172.31.0.20/31.",
        )
        option_a_properties_create.secondary_ipv6_prefix = AAZStrArg(
            options=["secondary-ipv6-prefix"],
            help="Secondary IPv6 Address Prefix of CE-PE interconnect links. Example : 3FFE:FFFF:0:CD30::a4/126.",
        )
        option_a_properties_create.vlan_id = AAZIntArg(
            options=["vlan-id"],
            help="Vlan Id. The value should be between 501 to 4095. Example : 501.",
            fmt=AAZIntArgFormat(
                maximum=4095,
                minimum=501,
            ),
        )

        _schema.mtu = cls._args_option_a_properties_create.mtu
        _schema.peer_asn = cls._args_option_a_properties_create.peer_asn
        _schema.primary_ipv4_prefix = cls._args_option_a_properties_create.primary_ipv4_prefix
        _schema.primary_ipv6_prefix = cls._args_option_a_properties_create.primary_ipv6_prefix
        _schema.secondary_ipv4_prefix = cls._args_option_a_properties_create.secondary_ipv4_prefix
        _schema.secondary_ipv6_prefix = cls._args_option_a_properties_create.secondary_ipv6_prefix
        _schema.vlan_id = cls._args_option_a_properties_create.vlan_id

    _args_option_b_properties_create = None

    @classmethod
    def _build_args_option_b_properties_create(cls, _schema):
        if cls._args_option_b_properties_create is not None:
            _schema.export_route_targets = cls._args_option_b_properties_create.export_route_targets
            _schema.import_route_targets = cls._args_option_b_properties_create.import_route_targets
            return

        cls._args_option_b_properties_create = AAZObjectArg()

        option_b_properties_create = cls._args_option_b_properties_create
        option_b_properties_create.export_route_targets = AAZListArg(
            options=["export-route-targets"],
            help="Route Targets to be applied for outgoing routes from CE. Example: 65541:2001.",
            required=True,
        )
        option_b_properties_create.import_route_targets = AAZListArg(
            options=["import-route-targets"],
            help="Route Targets to be applied for incoming routes into CE. Example: 65311:2001, 65412:2001.",
            required=True,
        )

        export_route_targets = cls._args_option_b_properties_create.export_route_targets
        export_route_targets.Element = AAZStrArg()

        import_route_targets = cls._args_option_b_properties_create.import_route_targets
        import_route_targets.Element = AAZStrArg()

        _schema.export_route_targets = cls._args_option_b_properties_create.export_route_targets
        _schema.import_route_targets = cls._args_option_b_properties_create.import_route_targets

    def _execute_operations(self):
        self.pre_operations()
        yield self.NetworkFabricsCreate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class NetworkFabricsCreate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkFabrics/{networkFabricName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "networkFabricName", self.ctx.args.resource_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-02-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("location", AAZStrType, ".location", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("annotation", AAZStrType, ".annotation")
                properties.set_prop("fabricASN", AAZIntType, ".fabric_asn", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("ipv4Prefix", AAZStrType, ".ipv4_prefix")
                properties.set_prop("ipv6Prefix", AAZStrType, ".ipv6_prefix")
                properties.set_prop("managementNetworkConfiguration", AAZObjectType, ".managed_network_config", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("networkFabricControllerId", AAZStrType, ".nfc_id", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("networkFabricSku", AAZStrType, ".nf_sku", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("rackCount", AAZIntType, ".rack_count", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("serverCountPerRack", AAZIntType, ".server_count_per_rack", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("terminalServerConfiguration", AAZObjectType, ".ts_config", typ_kwargs={"flags": {"required": True}})

            management_network_configuration = _builder.get(".properties.managementNetworkConfiguration")
            if management_network_configuration is not None:
                management_network_configuration.set_prop("infrastructureVpnConfiguration", AAZObjectType, ".infrastructure_vpn_configuration", typ_kwargs={"flags": {"required": True}})
                management_network_configuration.set_prop("workloadVpnConfiguration", AAZObjectType, ".workload_vpn_configuration", typ_kwargs={"flags": {"required": True}})

            infrastructure_vpn_configuration = _builder.get(".properties.managementNetworkConfiguration.infrastructureVpnConfiguration")
            if infrastructure_vpn_configuration is not None:
                _CreateHelper._build_schema_option_a_properties_create(infrastructure_vpn_configuration.set_prop("optionAProperties", AAZObjectType, ".option_a_properties"))
                _CreateHelper._build_schema_option_b_properties_create(infrastructure_vpn_configuration.set_prop("optionBProperties", AAZObjectType, ".option_b_properties"))
                infrastructure_vpn_configuration.set_prop("peeringOption", AAZStrType, ".peering_option", typ_kwargs={"flags": {"required": True}})

            workload_vpn_configuration = _builder.get(".properties.managementNetworkConfiguration.workloadVpnConfiguration")
            if workload_vpn_configuration is not None:
                _CreateHelper._build_schema_option_a_properties_create(workload_vpn_configuration.set_prop("optionAProperties", AAZObjectType, ".option_a_properties"))
                _CreateHelper._build_schema_option_b_properties_create(workload_vpn_configuration.set_prop("optionBProperties", AAZObjectType, ".option_b_properties"))
                workload_vpn_configuration.set_prop("peeringOption", AAZStrType, ".peering_option", typ_kwargs={"flags": {"required": True}})

            terminal_server_configuration = _builder.get(".properties.terminalServerConfiguration")
            if terminal_server_configuration is not None:
                terminal_server_configuration.set_prop("password", AAZStrType, ".password", typ_kwargs={"flags": {"required": True, "secret": True}})
                terminal_server_configuration.set_prop("primaryIpv4Prefix", AAZStrType, ".primary_ipv4_prefix", typ_kwargs={"flags": {"required": True}})
                terminal_server_configuration.set_prop("primaryIpv6Prefix", AAZStrType, ".primary_ipv6_prefix")
                terminal_server_configuration.set_prop("secondaryIpv4Prefix", AAZStrType, ".secondary_ipv4_prefix", typ_kwargs={"flags": {"required": True}})
                terminal_server_configuration.set_prop("secondaryIpv6Prefix", AAZStrType, ".secondary_ipv6_prefix")
                terminal_server_configuration.set_prop("serialNumber", AAZStrType, ".serial_number")
                terminal_server_configuration.set_prop("username", AAZStrType, ".username", typ_kwargs={"flags": {"required": True}})

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()

            _schema_on_200_201 = cls._schema_on_200_201
            _schema_on_200_201.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200_201.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200_201.tags = AAZDictType()
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties
            properties.annotation = AAZStrType()
            properties.fabric_asn = AAZIntType(
                serialized_name="fabricASN",
                flags={"required": True},
            )
            properties.ipv4_prefix = AAZStrType(
                serialized_name="ipv4Prefix",
            )
            properties.ipv6_prefix = AAZStrType(
                serialized_name="ipv6Prefix",
            )
            properties.l2_isolation_domains = AAZListType(
                serialized_name="l2IsolationDomains",
                flags={"read_only": True},
            )
            properties.l3_isolation_domains = AAZListType(
                serialized_name="l3IsolationDomains",
                flags={"read_only": True},
            )
            properties.management_network_configuration = AAZObjectType(
                serialized_name="managementNetworkConfiguration",
                flags={"required": True},
            )
            properties.network_fabric_controller_id = AAZStrType(
                serialized_name="networkFabricControllerId",
                flags={"required": True},
            )
            properties.network_fabric_sku = AAZStrType(
                serialized_name="networkFabricSku",
                flags={"required": True},
            )
            properties.operational_state = AAZStrType(
                serialized_name="operationalState",
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.rack_count = AAZIntType(
                serialized_name="rackCount",
                flags={"required": True},
            )
            properties.racks = AAZListType(
                flags={"read_only": True},
            )
            properties.router_id = AAZStrType(
                serialized_name="routerId",
                flags={"read_only": True},
            )
            properties.server_count_per_rack = AAZIntType(
                serialized_name="serverCountPerRack",
                flags={"required": True},
            )
            properties.terminal_server_configuration = AAZObjectType(
                serialized_name="terminalServerConfiguration",
                flags={"required": True},
            )

            l2_isolation_domains = cls._schema_on_200_201.properties.l2_isolation_domains
            l2_isolation_domains.Element = AAZStrType()

            l3_isolation_domains = cls._schema_on_200_201.properties.l3_isolation_domains
            l3_isolation_domains.Element = AAZStrType()

            management_network_configuration = cls._schema_on_200_201.properties.management_network_configuration
            management_network_configuration.infrastructure_vpn_configuration = AAZObjectType(
                serialized_name="infrastructureVpnConfiguration",
                flags={"required": True},
            )
            management_network_configuration.workload_vpn_configuration = AAZObjectType(
                serialized_name="workloadVpnConfiguration",
                flags={"required": True},
            )

            infrastructure_vpn_configuration = cls._schema_on_200_201.properties.management_network_configuration.infrastructure_vpn_configuration
            infrastructure_vpn_configuration.administrative_state = AAZStrType(
                serialized_name="administrativeState",
                flags={"read_only": True},
            )
            infrastructure_vpn_configuration.network_to_network_interconnect_id = AAZStrType(
                serialized_name="networkToNetworkInterconnectId",
                flags={"read_only": True},
            )
            infrastructure_vpn_configuration.option_a_properties = AAZObjectType(
                serialized_name="optionAProperties",
            )
            _CreateHelper._build_schema_option_a_properties_read(infrastructure_vpn_configuration.option_a_properties)
            infrastructure_vpn_configuration.option_b_properties = AAZObjectType(
                serialized_name="optionBProperties",
            )
            _CreateHelper._build_schema_option_b_properties_read(infrastructure_vpn_configuration.option_b_properties)
            infrastructure_vpn_configuration.peering_option = AAZStrType(
                serialized_name="peeringOption",
                flags={"required": True},
            )

            workload_vpn_configuration = cls._schema_on_200_201.properties.management_network_configuration.workload_vpn_configuration
            workload_vpn_configuration.administrative_state = AAZStrType(
                serialized_name="administrativeState",
                flags={"read_only": True},
            )
            workload_vpn_configuration.network_to_network_interconnect_id = AAZStrType(
                serialized_name="networkToNetworkInterconnectId",
                flags={"read_only": True},
            )
            workload_vpn_configuration.option_a_properties = AAZObjectType(
                serialized_name="optionAProperties",
            )
            _CreateHelper._build_schema_option_a_properties_read(workload_vpn_configuration.option_a_properties)
            workload_vpn_configuration.option_b_properties = AAZObjectType(
                serialized_name="optionBProperties",
            )
            _CreateHelper._build_schema_option_b_properties_read(workload_vpn_configuration.option_b_properties)
            workload_vpn_configuration.peering_option = AAZStrType(
                serialized_name="peeringOption",
                flags={"required": True},
            )

            racks = cls._schema_on_200_201.properties.racks
            racks.Element = AAZStrType()

            terminal_server_configuration = cls._schema_on_200_201.properties.terminal_server_configuration
            terminal_server_configuration.network_device_id = AAZStrType(
                serialized_name="networkDeviceId",
                flags={"read_only": True},
            )
            terminal_server_configuration.password = AAZStrType(
                flags={"required": True, "secret": True},
            )
            terminal_server_configuration.primary_ipv4_prefix = AAZStrType(
                serialized_name="primaryIpv4Prefix",
                flags={"required": True},
            )
            terminal_server_configuration.primary_ipv6_prefix = AAZStrType(
                serialized_name="primaryIpv6Prefix",
            )
            terminal_server_configuration.secondary_ipv4_prefix = AAZStrType(
                serialized_name="secondaryIpv4Prefix",
                flags={"required": True},
            )
            terminal_server_configuration.secondary_ipv6_prefix = AAZStrType(
                serialized_name="secondaryIpv6Prefix",
            )
            terminal_server_configuration.serial_number = AAZStrType(
                serialized_name="serialNumber",
            )
            terminal_server_configuration.username = AAZStrType(
                flags={"required": True},
            )

            system_data = cls._schema_on_200_201.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            tags = cls._schema_on_200_201.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200_201


class _CreateHelper:
    """Helper class for Create"""

    @classmethod
    def _build_schema_option_a_properties_create(cls, _builder):
        if _builder is None:
            return
        _builder.set_prop("mtu", AAZIntType, ".mtu")
        _builder.set_prop("peerASN", AAZIntType, ".peer_asn")
        _builder.set_prop("primaryIpv4Prefix", AAZStrType, ".primary_ipv4_prefix")
        _builder.set_prop("primaryIpv6Prefix", AAZStrType, ".primary_ipv6_prefix")
        _builder.set_prop("secondaryIpv4Prefix", AAZStrType, ".secondary_ipv4_prefix")
        _builder.set_prop("secondaryIpv6Prefix", AAZStrType, ".secondary_ipv6_prefix")
        _builder.set_prop("vlanId", AAZIntType, ".vlan_id")

    @classmethod
    def _build_schema_option_b_properties_create(cls, _builder):
        if _builder is None:
            return
        _builder.set_prop("exportRouteTargets", AAZListType, ".export_route_targets", typ_kwargs={"flags": {"required": True}})
        _builder.set_prop("importRouteTargets", AAZListType, ".import_route_targets", typ_kwargs={"flags": {"required": True}})

        export_route_targets = _builder.get(".exportRouteTargets")
        if export_route_targets is not None:
            export_route_targets.set_elements(AAZStrType, ".")

        import_route_targets = _builder.get(".importRouteTargets")
        if import_route_targets is not None:
            import_route_targets.set_elements(AAZStrType, ".")

    _schema_option_a_properties_read = None

    @classmethod
    def _build_schema_option_a_properties_read(cls, _schema):
        if cls._schema_option_a_properties_read is not None:
            _schema.bfd_configuration = cls._schema_option_a_properties_read.bfd_configuration
            _schema.mtu = cls._schema_option_a_properties_read.mtu
            _schema.peer_asn = cls._schema_option_a_properties_read.peer_asn
            _schema.primary_ipv4_prefix = cls._schema_option_a_properties_read.primary_ipv4_prefix
            _schema.primary_ipv6_prefix = cls._schema_option_a_properties_read.primary_ipv6_prefix
            _schema.secondary_ipv4_prefix = cls._schema_option_a_properties_read.secondary_ipv4_prefix
            _schema.secondary_ipv6_prefix = cls._schema_option_a_properties_read.secondary_ipv6_prefix
            _schema.vlan_id = cls._schema_option_a_properties_read.vlan_id
            return

        cls._schema_option_a_properties_read = _schema_option_a_properties_read = AAZObjectType()

        option_a_properties_read = _schema_option_a_properties_read
        option_a_properties_read.bfd_configuration = AAZObjectType(
            serialized_name="bfdConfiguration",
        )
        option_a_properties_read.mtu = AAZIntType()
        option_a_properties_read.peer_asn = AAZIntType(
            serialized_name="peerASN",
        )
        option_a_properties_read.primary_ipv4_prefix = AAZStrType(
            serialized_name="primaryIpv4Prefix",
        )
        option_a_properties_read.primary_ipv6_prefix = AAZStrType(
            serialized_name="primaryIpv6Prefix",
        )
        option_a_properties_read.secondary_ipv4_prefix = AAZStrType(
            serialized_name="secondaryIpv4Prefix",
        )
        option_a_properties_read.secondary_ipv6_prefix = AAZStrType(
            serialized_name="secondaryIpv6Prefix",
        )
        option_a_properties_read.vlan_id = AAZIntType(
            serialized_name="vlanId",
        )

        bfd_configuration = _schema_option_a_properties_read.bfd_configuration
        bfd_configuration.interval = AAZIntType(
            flags={"read_only": True},
        )
        bfd_configuration.multiplier = AAZIntType(
            flags={"read_only": True},
        )

        _schema.bfd_configuration = cls._schema_option_a_properties_read.bfd_configuration
        _schema.mtu = cls._schema_option_a_properties_read.mtu
        _schema.peer_asn = cls._schema_option_a_properties_read.peer_asn
        _schema.primary_ipv4_prefix = cls._schema_option_a_properties_read.primary_ipv4_prefix
        _schema.primary_ipv6_prefix = cls._schema_option_a_properties_read.primary_ipv6_prefix
        _schema.secondary_ipv4_prefix = cls._schema_option_a_properties_read.secondary_ipv4_prefix
        _schema.secondary_ipv6_prefix = cls._schema_option_a_properties_read.secondary_ipv6_prefix
        _schema.vlan_id = cls._schema_option_a_properties_read.vlan_id

    _schema_option_b_properties_read = None

    @classmethod
    def _build_schema_option_b_properties_read(cls, _schema):
        if cls._schema_option_b_properties_read is not None:
            _schema.export_route_targets = cls._schema_option_b_properties_read.export_route_targets
            _schema.import_route_targets = cls._schema_option_b_properties_read.import_route_targets
            return

        cls._schema_option_b_properties_read = _schema_option_b_properties_read = AAZObjectType()

        option_b_properties_read = _schema_option_b_properties_read
        option_b_properties_read.export_route_targets = AAZListType(
            serialized_name="exportRouteTargets",
            flags={"required": True},
        )
        option_b_properties_read.import_route_targets = AAZListType(
            serialized_name="importRouteTargets",
            flags={"required": True},
        )

        export_route_targets = _schema_option_b_properties_read.export_route_targets
        export_route_targets.Element = AAZStrType()

        import_route_targets = _schema_option_b_properties_read.import_route_targets
        import_route_targets.Element = AAZStrType()

        _schema.export_route_targets = cls._schema_option_b_properties_read.export_route_targets
        _schema.import_route_targets = cls._schema_option_b_properties_read.import_route_targets


__all__ = ["Create"]
