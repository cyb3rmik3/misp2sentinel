# TEST FILE - For Microsoft Defender for DevOps Secrets Protection Testing
# WARNING: This file intentionally contains fake/test credentials
# DO NOT use any of these values in production

# --- Azure Storage Account Key (fake) ---
AZURE_STORAGE_ACCOUNT_NAME = "mytestaccount"
AZURE_STORAGE_ACCOUNT_KEY = "dGVzdGtleWZvcmRlZmVuZGVydGVzdGluZ3B1cnBvc2VzIG9ubHkgbm90cmVhbA==+dGVzdGtleWZvcmRlZmVuZGVydGVzdA=="

# --- Azure SQL Connection String (fake) ---
AZURE_SQL_CONNECTION_STRING = "Server=tcp:mytestserver.database.windows.net,1433;Initial Catalog=mytestdb;Persist Security Info=False;User ID=testadmin;Password=FakeP@ssw0rd123!;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;"

# --- AWS Access Keys (fake) ---
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# --- GitHub Personal Access Token (fake) ---
GITHUB_TOKEN = "ghp_FakeTokenForTestingDefenderForDevOps1234"

# --- Generic API Key (fake) ---
API_KEY = "sk-FakeAPIKeyForTestingPurposesOnly1234567890abcdef"

# --- OAuth Client Secret (fake) ---
CLIENT_ID = "fake-client-id-1234-5678-abcd-efgh"
CLIENT_SECRET = "FakeClientSecret~abc123DEF456ghi789JKL"

# --- Private Key (fake/truncated) ---
PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEA2a2rwplBQLF29amygykEMmYz0+Kcj3bKBp29P2rFj7cB/OBN
THISISAFAKEKEYFORTESTINGDEFENDERFORDEVOPSSECRETPROTECTIONONLY==
-----END RSA PRIVATE KEY-----"""

# --- Slack Webhook (fake) ---
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/TXXXXXXXX/BXXXXXXXX/FakeSlackWebhookTokenForTesting"

# --- SendGrid API Key (fake) ---
SENDGRID_API_KEY = "SG.FakeKeyForTestingDefenderForDevOps.abcdefghijklmnopqrstuvwxyz1234567890"

# --- Main function ---
def main():
    print("This file is for testing Microsoft Defender for DevOps secrets protection.")
    print("All credentials in this file are FAKE and for testing purposes only.")

if __name__ == "__main__":
    main()
