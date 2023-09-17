from rest_framework_simplejwt.tokens import RefreshToken

class JWTToken:

    @staticmethod
    def get_tokens_for_user(user):
        """
            This function generates a pair of JWT tokens 
            (refresh token and access token) for the given user.
        """
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }