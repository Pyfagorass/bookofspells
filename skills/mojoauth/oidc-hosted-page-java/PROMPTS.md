# Suggested Prompts for MojoAuth OIDC — Java / Spring Boot

## Full Implementation

> "Add passwordless authentication to my Spring Boot application using MojoAuth.
>
> Follow `skills/authentication/oidc-hosted-page-java/SKILL.md` exactly.
>
> Requirements:
> 1. Add `spring-boot-starter-oauth2-client` dependency.
> 2. Configure `application.yml` with my MojoAuth Domain and credentials.
> 3. Set up Spring Security with OAuth2 login.
> 4. Create a login page with a 'Sign In with MojoAuth' link.
>
> My MojoAuth config:
> - MojoAuth Domain: `your-app.mojoauth.com`
> - Client ID: `<my_client_id>`
> - Redirect URI: `http://localhost:8080/login/oauth2/code/mojoauth`"

## Add MojoAuth to Existing Login

> "My Spring Boot app already has form login. Add MojoAuth as a passwordless alternative.
> Reference `skills/authentication/oidc-hosted-page-java/SKILL.md`.
> Both paths should result in the same Spring Security authentication."
