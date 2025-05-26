

print("[DeFooocus] Preparing ...")

theme = "dark" #@param ["dark", "light"]
preset = "deafult" #@param ["deafult", "realistic", "anime", "lcm", "sai", "turbo", "lighting", "hypersd", "playground_v2.5", "dpo", "spo", "sd1.5"]
advenced_args = "--share --attention-split --always-high-vram --disable-offload-from-vram --all-in-fp16" #@param {type: "string"}

if preset != "deafult":
  args = f"{advenced_args} --theme {theme} --preset {preset}"
else:
  args = f"{advenced_args} --theme {theme}"

!pip install -q pygit2==1.12.2
%cd /content
!git clone https://github.com/ehristoforu/DeFooocus.git
%cd /content/DeFooocus
!pip install -q -r requirements_versions.txt

print("[DeFooocus] Starting ...")
!python entry_with_update.py $args
