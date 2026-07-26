# Archetype: Mobile Application

## Default Stack Recommendation

| Layer | Default | Alternative | When to Switch |
|-------|---------|-------------|----------------|
| Framework | React Native (Expo) | Flutter | User prefers Dart, or needs pixel-perfect custom UI |
| Language | TypeScript | Dart (Flutter) | Only with Flutter |
| Navigation | Expo Router | React Navigation | Need more control than file-based routing |
| Styling | NativeWind (Tailwind) | StyleSheet | User doesn't know Tailwind |
| State | Zustand + TanStack Query | Redux Toolkit | Enterprise, team already uses Redux |
| Backend | Supabase | Firebase | Need Firestore, or Google ecosystem preference |
| Auth | Supabase Auth | Clerk Expo SDK, Firebase Auth | Clerk for social logins, Firebase for Google-heavy |
| Push Notifications | Expo Notifications | OneSignal | Advanced targeting/analytics |
| OTA Updates | EAS Update | CodePush | — |
| Build/Deploy | EAS Build | Fastlane | Existing Fastlane setup |
| Package Manager | npm (Expo default) | pnpm | — |

## Default Directory Structure (Expo Router)

```
app/
  (tabs)/
    index.tsx                  # Home tab
    explore.tsx                # Explore/search tab
    profile.tsx               # Profile tab
    _layout.tsx               # Tab bar layout
  (auth)/
    login.tsx                 # Login screen
    register.tsx              # Sign-up screen
    _layout.tsx               # Auth flow layout (no tabs)
  (modals)/
    [id].tsx                  # Detail modal
    settings.tsx              # Settings modal
  _layout.tsx                 # Root layout (auth check, providers)
  +not-found.tsx              # 404 screen
components/
  ui/                         # Reusable primitives (Button, Input, Card)
  screens/                    # Screen-specific components
  shared/                     # Shared across screens
lib/
  supabase.ts                 # Supabase client
  api.ts                      # API helper functions
  storage.ts                  # AsyncStorage utilities
hooks/
  useAuth.ts                  # Auth state hook
  useColorScheme.ts           # Dark/light mode
  use[Feature].ts             # Feature-specific hooks
constants/
  Colors.ts                   # Color tokens
  Layout.ts                   # Spacing, sizing constants
types/
  index.ts                    # Shared types
assets/
  images/                     # App images
  fonts/                      # Custom fonts
```

## Common Patterns

### Auth Flow
1. Root layout checks auth state → redirect to `/(auth)/login` or `/(tabs)/`
2. Login/register via Supabase Auth (email, Google, Apple sign-in)
3. Session persisted in SecureStore
4. Token refresh handled automatically by Supabase client

### Data Layer
- TanStack Query for server state (caching, refetching, optimistic updates)
- Zustand for client-only state (UI state, preferences)
- AsyncStorage for persistent local data

### Offline Support (if needed)
- TanStack Query's `persistQueryClient` with AsyncStorage
- Optimistic mutations with rollback on failure
- Network status indicator component

## Build Order

1. **Scaffolding**: `npx create-expo-app@latest`, install NativeWind, configure fonts
2. **Navigation**: Set up Expo Router — tabs layout, auth group, modal group
3. **Auth**: Supabase Auth setup, login/register screens, auth check in root layout
4. **Design system**: Color tokens, spacing, typography — NativeWind theme config
5. **Core screens**: Build the primary feature screen (list → detail pattern)
6. **Data layer**: Supabase queries wrapped in TanStack Query hooks
7. **Profile & Settings**: User profile screen, settings with preferences
8. **Push notifications**: Expo Notifications setup, permission handling
9. **Polish**: Loading skeletons, error states, haptic feedback, animations
10. **Testing**: Unit tests for business logic (Vitest), E2E for critical flows (Detox or Maestro)
11. **Build & Submit**: EAS Build config, app store metadata, TestFlight/Play Console

## Deployment Details

### EAS Build
- `eas build --platform ios` / `eas build --platform android`
- Configure `eas.json` with build profiles: development, preview, production
- Development builds include dev client for hot reloading
- Production builds are optimized and signed for app store submission

### App Store Submission
- **iOS**: EAS Submit → TestFlight → App Store Connect review (1-3 days)
- **Android**: EAS Submit → Google Play Console → review (hours to days)
- Prepare: app icon (1024x1024), screenshots per device size, privacy policy URL, app description

### OTA Updates (EAS Update)
- Push JS/asset updates without app store review
- `eas update --branch production` for instant patches
- Cannot change native code (only JS bundle + assets)
- Use for: bug fixes, content updates, minor UI tweaks

## Common Pitfalls

- **Don't eject from Expo** unless you absolutely need a native module that isn't supported. Expo SDK covers 95% of use cases.
- **Don't ignore platform differences.** Test on both iOS and Android. Safe areas, keyboard behavior, and gesture handling differ.
- **Don't skip app store guidelines.** Apple and Google review can reject. Know the rules upfront.
- **Don't use web-only libraries.** Check that every package supports React Native before installing.
- **Don't neglect deep linking.** Set up universal links early — retrofitting is painful.

## Skills for Build Phase

| Skill | When |
|-------|------|
| `/ui-ux-pro-max` | Design system and component styling |
| `/deep-research` | Platform-specific best practices |

## See Also

- `knowledge/building-blocks/auth-patterns.md` — Mobile auth patterns (Supabase Auth, Firebase Auth)
- `knowledge/building-blocks/state-management.md` — TanStack Query + Zustand for mobile
- `knowledge/building-blocks/api-design-patterns.md` — If building the backend API too
- `knowledge/building-blocks/testing-patterns.md` — Mobile testing with Detox/Maestro
