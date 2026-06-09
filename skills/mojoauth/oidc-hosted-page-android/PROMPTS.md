# Suggested Prompts for MojoAuth OIDC — Android

## Full Implementation

> "Add passwordless authentication to my Android application using MojoAuth.
>
> Follow `skills/authentication/oidc-hosted-page-android/SKILL.md` exactly.
>
> Requirements:
> 1. Add AppAuth dependency (`net.openid:appauth`).
> 2. Configure the redirect scheme and AndroidManifest.
> 3. Create a login screen with a 'Sign In with MojoAuth' button.
> 4. Implement the OIDC flow with PKCE and token exchange.
>
> My MojoAuth config:
> - MojoAuth Domain: `your-app.mojoauth.com`
> - Client ID: `<my_client_id>`
> - Redirect URI: `com.example.myapp://auth/callback`"

## Add MojoAuth to Existing Login

> "My Android app already has a login screen. Add MojoAuth as a passwordless alternative.
> Reference `skills/authentication/oidc-hosted-page-android/SKILL.md`.
> The MojoAuth flow should use AppAuth and PKCE."
