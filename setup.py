#  Licensed to the Apache Software Foundation (ASF) under one or more
#  contributor license agreements. See the NOTICE file distributed with
#  this work for additional information regarding copyright ownership.
#  The ASF licenses this file to You under the Apache License, Version 2.0
#  (the "License"); you may not use this file except in compliance with
#  the License. You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from typing import Dict, Set
import os

from setuptools import setup, find_namespace_packages


def get_version():
    root = os.path.dirname(__file__)
    changelog = os.path.join(root, "CHANGELOG")
    with open(changelog) as f:
        return f.readline().strip()


def get_long_description():
    root = os.path.dirname(__file__)
    with open(os.path.join(root, "README.md")) as f:
        description = f.read()
    description += "\n\nChangelog\n=========\n\n"
    with open(os.path.join(root, "CHANGELOG")) as f:
        description += f.read()
    return description


with open("requirements.txt") as f:
    required = f.read().splitlines()

build_options = {"includes": ["_cffi_backend"]}
setup(
    name="openmetadata-data-profiler",
    version="0.0.1",
    url="https://open-metadata.org/",
    author="OpenMetadata Committers",
    license="Apache License 2.0",
    description="Data Profiler Library for OpenMetadata",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    python_requires=">=3.8",
    options={"build_exe": build_options},
    package_dir={"": "src"},
    zip_safe=False,
    dependency_links=[
    ],
    project_urls={
        "Documentation": "https://docs.open-metadata.org/",
        "Source": "https://github.com/open-metadata/data-profiler",
    },
    packages=find_namespace_packages(where='./src', exclude=['tests*']),
    entry_points={
        "console_scripts": ["metadata = metadata.cmd:metadata"],
    },
    install_requires=required,
    extras_require={
        "spark": ["pyspark>=2.3.2"],
        "sqlalchemy": ["sqlalchemy>=1.3.16"],
        "airflow": ["apache-airflow[s3]>=1.9.0", "boto3>=1.7.3"],
        "gcp": [
            "google-cloud>=0.34.0",
            "google-cloud-storage>=1.28.0",
            "google-cloud-secret-manager>=1.0.0",
            "pybigquery==0.4.15",
        ],
        "redshift": ["psycopg2>=2.8"],
        "s3": ["boto3>=1.14"],
        "aws_secrets": ["boto3>=1.8.7"],
        "azure_secrets": ["azure-identity>=1.0.0", "azure-keyvault-secrets>=4.0.0"],
        "snowflake": ["snowflake-sqlalchemy>=1.2"],
    }

)
