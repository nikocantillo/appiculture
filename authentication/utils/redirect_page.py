from django.shortcuts import redirect


class RedirectPage():

    def __init__(self, target_slug, session) -> None:

        self.target_slug = target_slug
        self.session = session

    def validate(self):

        session_user = self.session.get('user_data')

        if session_user is None:
            return False
        return True

    def redirect_page(self):

        if not self.validate():

            return redirect(self.target_slug)

    def origin_redirect(self):

        origin_url = self.target_slug

        if origin_url is not None:

            if self.validate():

                return redirect(self.target_slug)

        return False
