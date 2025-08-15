import runpod

def handler(event):
    # 클라이언트가 보낸 입력 읽기
    name = event.get("input", {}).get("name", "world")
    # 여기서부터 모델 호출/로직을 점점 붙여나가면 됩니다.
    return {"message": f"Hello, {name}!"}

# RunPod 서버리스 런타임 시작
runpod.serverless.start({"handler": handler})
