# Suggested Prompts for MojoAuth OIDC — .NET Core

## Full Implementation

> "Add passwordless authentication to my ASP.NET Core application using MojoAuth.
>
> Follow `skills/authentication/oidc-hosted-page-dotnet/SKILL.md` exactly.
>
> Requirements:
> 1. Install `Microsoft.AspNetCore.Authentication.OpenIdConnect`.
> 2. Configure the OIDC middleware with my MojoAuth Domain and credentials.
> 3. Create a login page with a 'Sign In with MojoAuth' button.
> 4. Set up the callback path for OIDC redirect handling.
>
> My MojoAuth config:
> - MojoAuth Domain: `your-app.mojoauth.com`
> - Client ID: `<my_client_id>`
> - Redirect URI: `http://localhost:5000/auth/callback`"

## Add MojoAuth to Existing Login

> "My ASP.NET Core app already has Identity login. Add MojoAuth as a passwordless alternative.
> Reference `skills/authentication/oidc-hosted-page-dotnet/SKILL.md`.
> Both paths should result in the same ClaimsPrincipal."
