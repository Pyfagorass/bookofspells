# Suggested Prompts for MojoAuth OIDC — Laravel

## Full Implementation

> "Add passwordless authentication to my Laravel application using MojoAuth.
>
> Follow `skills/authentication/oidc-hosted-page-laravel/SKILL.md` exactly.
>
> Requirements:
> 1. Install `laravel/socialite`.
> 2. Create a MojoAuth Socialite provider.
> 3. Create a login page with a 'Sign In with MojoAuth' link.
> 4. Handle the OIDC callback and create/update the user.
>
> My MojoAuth config:
> - MojoAuth Domain: `your-app.mojoauth.com`
> - Client ID: `<my_client_id>`
> - Redirect URI: `http://localhost:8000/auth/callback`"

## Add MojoAuth to Existing Login

> "My Laravel app already has Breeze/Jetstream auth. Add MojoAuth as a passwordless alternative.
> Reference `skills/authentication/oidc-hosted-page-laravel/SKILL.md`.
> Both paths should result in the same Auth::login() session."
