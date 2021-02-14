AWSTemplateFormatVersion: 2010-09-09
Metadata:
  'AWS::CloudFormation::Designer':
    0768704d-1b5b-4dc5-99c0-6967ef8929a5:
      size:
        width: 660
        height: 330
      position:
        x: 130
        'y': 190
      z: 1
      embeds:
        - c8ab5f2e-b82b-4ee3-8910-f40e4cfd3cc6
        - 29fa4dc4-93da-46d1-99a9-0f1c2d818752
        - b948d785-decc-4677-b065-c1aa39cb87b5
    b948d785-decc-4677-b065-c1aa39cb87b5:
      size:
        width: 180
        height: 120
      position:
        x: 280
        'y': 190
      z: 2
      parent: 0768704d-1b5b-4dc5-99c0-6967ef8929a5
      embeds:
        - 6443ef65-1f73-4d81-87dd-7692c15e6eff
      iscontainedinside:
        - 0768704d-1b5b-4dc5-99c0-6967ef8929a5
        - 0768704d-1b5b-4dc5-99c0-6967ef8929a5
        - 0768704d-1b5b-4dc5-99c0-6967ef8929a5
        - 0768704d-1b5b-4dc5-99c0-6967ef8929a5
        - 0768704d-1b5b-4dc5-99c0-6967ef8929a5
        - 0768704d-1b5b-4dc5-99c0-6967ef8929a5
    6443ef65-1f73-4d81-87dd-7692c15e6eff:
      size:
        width: 60
        height: 60
      position:
        x: 370
        'y': 220
      z: 3
      parent: b948d785-decc-4677-b065-c1aa39cb87b5
      embeds: []
      iscontainedinside:
        - b948d785-decc-4677-b065-c1aa39cb87b5
        - b948d785-decc-4677-b065-c1aa39cb87b5
        - b948d785-decc-4677-b065-c1aa39cb87b5
        - b948d785-decc-4677-b065-c1aa39cb87b5
        - b948d785-decc-4677-b065-c1aa39cb87b5
      dependson:
        - e5520b31-4517-44ef-b593-228c4686d4af
    29fa4dc4-93da-46d1-99a9-0f1c2d818752:
      size:
        width: 60
        height: 60
      position:
        x: 430
        'y': 370
      z: 2
      parent: 0768704d-1b5b-4dc5-99c0-6967ef8929a5
      embeds: []
      iscontainedinside:
        - 0768704d-1b5b-4dc5-99c0-6967ef8929a5
        - 0768704d-1b5b-4dc5-99c0-6967ef8929a5
        - 0768704d-1b5b-4dc5-99c0-6967ef8929a5
        - 0768704d-1b5b-4dc5-99c0-6967ef8929a5
        - 0768704d-1b5b-4dc5-99c0-6967ef8929a5
        - 0768704d-1b5b-4dc5-99c0-6967ef8929a5
    f69bb300-ca8c-4e51-a1ad-b5679c97bee2:
      size:
        width: 60
        height: 60
      position:
        x: 30
        'y': 90
      z: 1
      embeds: []
    37225343-5425-48b6-9676-918d1a48d79f:
      source:
        id: 0768704d-1b5b-4dc5-99c0-6967ef8929a5
      target:
        id: f69bb300-ca8c-4e51-a1ad-b5679c97bee2
      z: 0
    c8ab5f2e-b82b-4ee3-8910-f40e4cfd3cc6:
      size:
        width: 120
        height: 90
      position:
        x: 210
        'y': 390
      z: 2
      parent: 0768704d-1b5b-4dc5-99c0-6967ef8929a5
      embeds:
        - e5520b31-4517-44ef-b593-228c4686d4af
      iscontainedinside:
        - 0768704d-1b5b-4dc5-99c0-6967ef8929a5
        - 0768704d-1b5b-4dc5-99c0-6967ef8929a5
        - 0768704d-1b5b-4dc5-99c0-6967ef8929a5
        - 0768704d-1b5b-4dc5-99c0-6967ef8929a5
        - 0768704d-1b5b-4dc5-99c0-6967ef8929a5
        - 0768704d-1b5b-4dc5-99c0-6967ef8929a5
    e5520b31-4517-44ef-b593-228c4686d4af:
      size:
        width: 60
        height: 60
      position:
        x: 240
        'y': 390
      z: 3
      parent: c8ab5f2e-b82b-4ee3-8910-f40e4cfd3cc6
      embeds: []
      isassociatedwith:
        - f69bb300-ca8c-4e51-a1ad-b5679c97bee2
      iscontainedinside:
        - c8ab5f2e-b82b-4ee3-8910-f40e4cfd3cc6
        - c8ab5f2e-b82b-4ee3-8910-f40e4cfd3cc6
        - c8ab5f2e-b82b-4ee3-8910-f40e4cfd3cc6
        - c8ab5f2e-b82b-4ee3-8910-f40e4cfd3cc6
        - c8ab5f2e-b82b-4ee3-8910-f40e4cfd3cc6
        - c8ab5f2e-b82b-4ee3-8910-f40e4cfd3cc6
      dependson:
        - 37225343-5425-48b6-9676-918d1a48d79f
    5cf81fbf-b49a-4adb-ae7b-c7ecdaa90da9:
      source:
        id: c8ab5f2e-b82b-4ee3-8910-f40e4cfd3cc6
      target:
        id: b948d785-decc-4677-b065-c1aa39cb87b5
      z: 1
Resources:
  VPC:
    Type: 'AWS::EC2::VPC'
    Properties:
      EnableDnsSupport: 'true'
      EnableDnsHostnames: 'true'
      CidrBlock: 10.0.0.0/16
    Metadata:
      'AWS::CloudFormation::Designer':
        id: 0768704d-1b5b-4dc5-99c0-6967ef8929a5
  PublicNet:
    Type: 'AWS::EC2::Subnet'
    Properties:
      VpcId: !Ref VPC
      CidrBlock: 10.0.0.0/24
    Metadata:
      'AWS::CloudFormation::Designer':
        id: b948d785-decc-4677-b065-c1aa39cb87b5
  WebServerInstance01:
    Type: 'AWS::EC2::Instance'
    Properties:
      InstanceType: !Ref InstanceType
      ImageId: !FindInMap 
        - AWSRegionArch2AMI
        - !Ref 'AWS::Region'
        - !FindInMap 
          - AWSInstanceType2Arch
          - !Ref InstanceType
          - Arch
      KeyName: !Ref KeyName
      NetworkInterfaces:
        - GroupSet:
            - !Ref WebServerSecurityGroup
          AssociatePublicIpAddress: 'true'
          DeviceIndex: '0'
          DeleteOnTermination: 'true'
          SubnetId: !Ref PublicNet
      Tags:
        - Key: Name
          Value: tomcat-node01
      UserData: !Base64 
        'Fn::Join':
          - ''
          - - |
              #!/bin/bash -xe
            - |
              yum install -y aws-cfn-bootstrap
            - |
              # Install the files and packages from the metadata
            - '/opt/aws/bin/cfn-init -v '
            - '         --stack '
            - !Ref 'AWS::StackName'
            - '         --resource WebServerInstance01 '
            - '         --configsets All '
            - '         --region '
            - !Ref 'AWS::Region'
            - |+

            - |
              # Signal the status from cfn-init
            - '/opt/aws/bin/cfn-signal -e $? '
            - '         --stack '
            - !Ref 'AWS::StackName'
            - '         --resource WebServerInstance01 '
            - '         --region '
            - !Ref 'AWS::Region'
            - |+

    Metadata:
      'AWS::CloudFormation::Designer':
        id: 6443ef65-1f73-4d81-87dd-7692c15e6eff
      'AWS::CloudFormation::Init':
        configSets:
          All:
            - ConfigureSampleApp
        ConfigureSampleApp:
          packages:
            yum:
              httpd: []
          files:
            /var/www/html/index.html:
              content: !Join 
                - |+

                - - >-
                    <h1>Congratulations Cloudelevation trainees, you have
                    successfully launched the AWS CloudFormation
                    sample.....</h1>
              mode: '000644'
              owner: root
              group: root
          services:
            sysvinit:
              httpd:
                enabled: 'true'
                ensureRunning: 'true'
  WebServerInstance02:
    Type: 'AWS::EC2::Instance'
    Properties:
      InstanceType: !Ref InstanceType
      ImageId: !FindInMap 
        - AWSRegionArch2AMI
        - !Ref 'AWS::Region'
        - !FindInMap 
          - AWSInstanceType2Arch
          - !Ref InstanceType
          - Arch
      KeyName: !Ref KeyName
      NetworkInterfaces:
        - GroupSet:
            - !Ref WebServerSecurityGroup
          AssociatePublicIpAddress: 'true'
          DeviceIndex: '0'
          DeleteOnTermination: 'true'
          SubnetId: !Ref PublicNet
      Tags:
        - Key: Name
          Value: tomcat-node02
      UserData: !Base64 
        'Fn::Join':
          - ''
          - - |
              #!/bin/bash -xe
            - |
              yum install -y aws-cfn-bootstrap
            - |
              # Install the files and packages from the metadata
            - '/opt/aws/bin/cfn-init -v '
            - '         --stack '
            - !Ref 'AWS::StackName'
            - '         --resource WebServerInstance02 '
            - '         --configsets All '
            - '         --region '
            - !Ref 'AWS::Region'
            - |+

            - |
              # Signal the status from cfn-init
            - '/opt/aws/bin/cfn-signal -e $? '
            - '         --stack '
            - !Ref 'AWS::StackName'
            - '         --resource WebServerInstance02 '
            - '         --region '
            - !Ref 'AWS::Region'
            - |+

    Metadata:
      'AWS::CloudFormation::Designer':
        id: 6443ef65-1f73-4d81-87dd-7692c15e6eff
      'AWS::CloudFormation::Init':
        configSets:
          All:
            - ConfigureSampleApp
        ConfigureSampleApp:
          packages:
            yum:
              httpd: []
          files:
            /var/www/html/index.html:
              content: !Join 
                - |+

                - - >-
                    <h1>Congratulations Cloudelevation trainees, you have
                    successfully launched the AWS CloudFormation
                    sample.....</h1>
              mode: '000644'
              owner: root
              group: root
          services:
            sysvinit:
              httpd:
                enabled: 'true'
                ensureRunning: 'true'
  WebServerSecurityGroup:
    Type: 'AWS::EC2::SecurityGroup'
    Properties:
      VpcId: !Ref VPC
      GroupDescription: Allow access from HTTP and SSH traffic
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: '80'
          ToPort: '8080'
          CidrIp: 0.0.0.0/0
        - IpProtocol: tcp
          FromPort: '22'
          ToPort: '22'
          CidrIp: !Ref SSHLocation
    Metadata:
      'AWS::CloudFormation::Designer':
        id: 29fa4dc4-93da-46d1-99a9-0f1c2d818752
  InternetGateway:
    Type: 'AWS::EC2::InternetGateway'
    Properties: {}
    Metadata:
      'AWS::CloudFormation::Designer':
        id: f69bb300-ca8c-4e51-a1ad-b5679c97bee2
  EC2VPCG99XT:
    Type: 'AWS::EC2::VPCGatewayAttachment'
    Properties:
      InternetGatewayId: !Ref InternetGateway
      VpcId: !Ref VPC
    Metadata:
      'AWS::CloudFormation::Designer':
        id: 37225343-5425-48b6-9676-918d1a48d79f
  PublicRouteTable:
    Type: 'AWS::EC2::RouteTable'
    Properties:
      VpcId: !Ref VPC
    Metadata:
      'AWS::CloudFormation::Designer':
        id: c8ab5f2e-b82b-4ee3-8910-f40e4cfd3cc6
  EC2R4YIAU:
    Type: 'AWS::EC2::Route'
    Properties:
      DestinationCidrBlock: 0.0.0.0/0
      RouteTableId: !Ref PublicRouteTable
      GatewayId: !Ref InternetGateway
    Metadata:
      'AWS::CloudFormation::Designer':
        id: e5520b31-4517-44ef-b593-228c4686d4af
    DependsOn:
      - EC2VPCG99XT
  EC2SRTA3I5CY:
    Type: 'AWS::EC2::SubnetRouteTableAssociation'
    Properties:
      RouteTableId: !Ref PublicRouteTable
      SubnetId: !Ref PublicNet
    Metadata:
      'AWS::CloudFormation::Designer':
        id: 5cf81fbf-b49a-4adb-ae7b-c7ecdaa90da9
Outputs:
  URL01:
    Value: !Join 
      - ''
      - - 'http://'
        - !GetAtt 
          - WebServerInstance01
          - PublicIp
    Description: Newly created application URL for WebSerberInstance-1
  URL02:
    Value: !Join 
      - ''
      - - 'http://'
        - !GetAtt 
          - WebServerInstance02
          - PublicIp
    Description: Newly created application URL for WebSerberInstance-2
Parameters:
  InstanceType:
    Description: WebServer EC2 instance type
    Type: String
    Default: t2.small
    AllowedValues:
      - t1.micro
      - t2.nano
      - t2.micro
      - t2.small
      - t2.medium
      - t2.large
      - m1.small
      - m1.medium
      - m1.large
      - m1.xlarge
      - m2.xlarge
      - m2.2xlarge
      - m2.4xlarge
      - m3.medium
      - m3.large
      - m3.xlarge
      - m3.2xlarge
      - m4.large
      - m4.xlarge
      - m4.2xlarge
      - m4.4xlarge
      - m4.10xlarge
      - c1.medium
      - c1.xlarge
      - c3.large
      - c3.xlarge
      - c3.2xlarge
      - c3.4xlarge
      - c3.8xlarge
      - c4.large
      - c4.xlarge
      - c4.2xlarge
      - c4.4xlarge
      - c4.8xlarge
      - g2.2xlarge
      - g2.8xlarge
      - r3.large
      - r3.xlarge
      - r3.2xlarge
      - r3.4xlarge
      - r3.8xlarge
      - i2.xlarge
      - i2.2xlarge
      - i2.4xlarge
      - i2.8xlarge
      - d2.xlarge
      - d2.2xlarge
      - d2.4xlarge
      - d2.8xlarge
      - hi1.4xlarge
      - hs1.8xlarge
      - cr1.8xlarge
      - cc2.8xlarge
      - cg1.4xlarge
    ConstraintDescription: must be a valid EC2 instance type.
  KeyName:
    Description: Name of an EC2 KeyPair to enable SSH access to the instance.
    Type: 'AWS::EC2::KeyPair::KeyName'
    ConstraintDescription: must be the name of an existing EC2 KeyPair.
  SSHLocation:
    Description: ' The IP address range that can be used to access the web server using SSH.'
    Type: String
    MinLength: '9'
    MaxLength: '18'
    Default: 0.0.0.0/0
    AllowedPattern: '(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})/(\d{1,2})'
    ConstraintDescription: must be a valid IP CIDR range of the form x.x.x.x/x.
Mappings:
  AWSInstanceType2Arch:
    t1.micro:
      Arch: HVM64
    t2.nano:
      Arch: HVM64
    t2.micro:
      Arch: HVM64
    t2.small:
      Arch: HVM64
    t2.medium:
      Arch: HVM64
    t2.large:
      Arch: HVM64
    m1.small:
      Arch: HVM64
    m1.medium:
      Arch: HVM64
    m1.large:
      Arch: HVM64
    m1.xlarge:
      Arch: HVM64
    m2.xlarge:
      Arch: HVM64
    m2.2xlarge:
      Arch: HVM64
    m2.4xlarge:
      Arch: HVM64
    m3.medium:
      Arch: HVM64
    m3.large:
      Arch: HVM64
    m3.xlarge:
      Arch: HVM64
    m3.2xlarge:
      Arch: HVM64
    m4.large:
      Arch: HVM64
    m4.xlarge:
      Arch: HVM64
    m4.2xlarge:
      Arch: HVM64
    m4.4xlarge:
      Arch: HVM64
    m4.10xlarge:
      Arch: HVM64
    c1.medium:
      Arch: HVM64
    c1.xlarge:
      Arch: HVM64
    c3.large:
      Arch: HVM64
    c3.xlarge:
      Arch: HVM64
    c3.2xlarge:
      Arch: HVM64
    c3.4xlarge:
      Arch: HVM64
    c3.8xlarge:
      Arch: HVM64
    c4.large:
      Arch: HVM64
    c4.xlarge:
      Arch: HVM64
    c4.2xlarge:
      Arch: HVM64
    c4.4xlarge:
      Arch: HVM64
    c4.8xlarge:
      Arch: HVM64
    g2.2xlarge:
      Arch: HVMG2
    g2.8xlarge:
      Arch: HVMG2
    r3.large:
      Arch: HVM64
    r3.xlarge:
      Arch: HVM64
    r3.2xlarge:
      Arch: HVM64
    r3.4xlarge:
      Arch: HVM64
    r3.8xlarge:
      Arch: HVM64
    i2.xlarge:
      Arch: HVM64
    i2.2xlarge:
      Arch: HVM64
    i2.4xlarge:
      Arch: HVM64
    i2.8xlarge:
      Arch: HVM64
    d2.xlarge:
      Arch: HVM64
    d2.2xlarge:
      Arch: HVM64
    d2.4xlarge:
      Arch: HVM64
    d2.8xlarge:
      Arch: HVM64
    hi1.4xlarge:
      Arch: HVM64
    hs1.8xlarge:
      Arch: HVM64
    cr1.8xlarge:
      Arch: HVM64
    cc2.8xlarge:
      Arch: HVM64
  AWSRegionArch2AMI:
    us-east-1:
      HVM64: ami-0885b1f6bd170450c
      HVMG2: ami-0a584ac55a7631c0c
    us-west-2:
      HVM64: ami-a0cfeed8
      HVMG2: ami-0e09505bc235aa82d
    us-west-1:
      HVM64: ami-0bdb828fd58c52235
      HVMG2: ami-066ee5fd4a9ef77f1
    eu-west-1:
      HVM64: ami-047bb4163c506cd98
      HVMG2: ami-0a7c483d527806435
    eu-west-2:
      HVM64: ami-f976839e
      HVMG2: NOT_SUPPORTED
    eu-west-3:
      HVM64: ami-0ebc281c20e89ba4b
      HVMG2: NOT_SUPPORTED
    eu-central-1:
      HVM64: ami-0233214e13e500f77
      HVMG2: ami-06223d46a6d0661c7
    ap-northeast-1:
      HVM64: ami-06cd52961ce9f0d85
      HVMG2: ami-053cdd503598e4a9d
    ap-northeast-2:
      HVM64: ami-0a10b2721688ce9d2
      HVMG2: NOT_SUPPORTED
    ap-northeast-3:
      HVM64: ami-0d98120a9fb693f07
      HVMG2: NOT_SUPPORTED
    ap-southeast-1:
      HVM64: ami-08569b978cc4dfa10
      HVMG2: ami-0be9df32ae9f92309
    ap-southeast-2:
      HVM64: ami-09b42976632b27e9b
      HVMG2: ami-0a9ce9fecc3d1daf8
    ap-south-1:
      HVM64: ami-0912f71e06545ad88
      HVMG2: ami-097b15e89dbdcfcf4
    us-east-2:
      HVM64: ami-0b59bfac6be064b78
      HVMG2: NOT_SUPPORTED
    ca-central-1:
      HVM64: ami-0b18956f
      HVMG2: NOT_SUPPORTED
    sa-east-1:
      HVM64: ami-07b14488da8ea02a0
      HVMG2: NOT_SUPPORTED
    cn-north-1:
      HVM64: ami-0a4eaf6c4454eda75
      HVMG2: NOT_SUPPORTED
    cn-northwest-1:
      HVM64: ami-6b6a7d09
      HVMG2: NOT_SUPPORTED
