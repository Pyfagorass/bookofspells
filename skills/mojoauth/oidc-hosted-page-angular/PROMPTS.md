# Suggested Prompts for MojoAuth OIDC — Angular

## Full Implementation

> "Add passwordless authentication to my Angular application using MojoAuth.
>
> Follow `skills/authentication/oidc-hosted-page-angular/SKILL.md` exactly.
>
> Requirements:
> 1. Install `angular-auth-oidc-client`.
> 2. Configure the OIDC module with my MojoAuth Domain and Client ID.
> 3. Create a login component with a 'Sign In with MojoAuth' button.
> 4. Create an auth callback component and configure the route.
> 5. Set up route guards for protected pages.
>
> My MojoAuth config:
> - MojoAuth Domain: `your-app.mojoauth.com`
> - Client ID: `<my_client_id>`
> - Redirect URI: `http://localhost:4200/auth/callback`"

## Add MojoAuth to Existing Login

> "My Angular app already has a login form. Add MojoAuth as a passwordless alternative.
> Reference `skills/authentication/oidc-hosted-page-angular/SKILL.md`.
> Both paths should result in the same authenticated state."
