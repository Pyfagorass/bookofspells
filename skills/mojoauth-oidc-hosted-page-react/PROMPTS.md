# Suggested Prompts for MojoAuth OIDC — React

## Full Implementation

> "Add passwordless authentication to my React application using MojoAuth.
>
> Follow `skills/authentication/oidc-hosted-page-react/SKILL.md` exactly.
>
> Requirements:
> 1. Install `oidc-client-ts`, `react-oidc-context`, and `react-router-dom`.
> 2. Configure the OIDC provider and wrap my app with `<AuthProvider>`.
> 3. Create a login page with a 'Sign In with MojoAuth' button.
> 4. Use `auth.signinRedirect()` to redirect to MojoAuth Hosted Login Page.
> 5. Create an `AuthCallback` component that checks auth state and navigates.
> 6. Set up the route for `/auth/callback`.
>
> My MojoAuth config:
> - MojoAuth Domain: `your-app.mojoauth.com`
> - Client ID: `<my_client_id>`
> - Redirect URI: `http://localhost:5173/auth/callback`"

## Add MojoAuth to Existing Login

> "My React app already has a custom auth context with JWT login. Add MojoAuth as a passwordless alternative.
> Reference `skills/authentication/oidc-hosted-page-react/SKILL.md`.
> Both paths should result in the same authenticated state in my auth context."
