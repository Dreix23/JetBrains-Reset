import flet as ft
from controllers.trial_reset_controller import TrialResetController
from views.trial_reset_view import TrialResetView

if __name__ == "__main__":
    controller = TrialResetController()
    view = TrialResetView(controller)
    ft.app(target=view.main, assets_dir="assets")
