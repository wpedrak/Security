Class | Threat | Mitigation
---|---|---
Spoofing | Fake admin page | SAML2 based authentication
Tampering | Wrong data about position is transmited (scooter can be anywhere) | daily audits
Repudation | Someone denied that he was using scooter | Signature on every action
Information Disclosure | Data is stolen from cloud provider | Encryption of data
Denial of Service | Cloud DB isn't available | Replicas in another zones/regions/cloud providers
Elevation of Privilege | Scooter is missconfigured and enables too many options (for example, debuging) | configuration checkers