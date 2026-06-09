# Suggested Prompts for MojoAuth M2M Authentication

## Full Implementation

> "I need to authenticate my backend service with a MojoAuth-protected API using Machine-to-Machine credentials.
>
> Follow `skills/authentication/m2m-client-credentials/SKILL.md` exactly.
>
> Requirements:
> - Use the Client Credentials grant to obtain an access token.
> - Cache the token and reuse until expiry.
> - Use the token to call my protected API at `<my_api_endpoint>`.
>
> My M2M credentials:
> - Client ID: `<service_client_id>`
> - Client Secret: `<service_client_secret>`
> - Token Endpoint: `https://your-app.mojoauth.com/oauth2/token`"

## Multi-Language Implementation

> "Show me how to implement MojoAuth M2M authentication in **{language}**.
> Reference `skills/authentication/m2m-client-credentials/SKILL.md` for the implementation pattern.
> Include token caching for production use."
