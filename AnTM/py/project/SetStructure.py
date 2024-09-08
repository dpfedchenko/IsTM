import Vacuum, LiquidCrystal, LiquidCrystal2, LinearDefect, TwistDefect

Structure = ["V", "LC", "LD", "LC", "V"]

StructureProperties = {
  "V": [Vacuum.epsilon_o, Vacuum.mu_o, Vacuum.epsilon_e, Vacuum.mu_e],
  "LC": [LiquidCrystal.epsilon_o, LiquidCrystal.mu_o, LiquidCrystal.epsilon_e, LiquidCrystal.mu_e],
  "LD": [LinearDefect.epsilon_o, LinearDefect.mu_o, LinearDefect.epsilon_e, LinearDefect.mu_e],
  "TD": [TwistDefect.epsilon_o, TwistDefect.mu_o, TwistDefect.epsilon_e, TwistDefect.mu_e],
  "LC2": [LiquidCrystal2.epsilon_o, LiquidCrystal2.mu_o, LiquidCrystal2.epsilon_e, LiquidCrystal2.mu_e],
  }