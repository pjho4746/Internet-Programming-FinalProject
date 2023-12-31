영양제 구입 사이트 프로젝트 
---
### 📍 프로젝트 소개
해당 프로젝트는 인터넷 프로그래밍 수업에서 배운 내용을 기반으로 진행한 기말 프로젝트입니다. 영양제 구입 사이트는 사용자들이 편리하게 영양제를 구매할 수 있도록 다양한 기능을 제공합니다.<br><br>

**해당 프로젝트는 삭제되어 git에 업로드되지 않았습니다. README 파일만 활동 내용을 정리한 문서입니다.*
   
### 📍 참고 자료
- 네이버 쇼핑 <헬시> 

### 📍 요구 사항
**1. 페이지 구성**
- 홈 페이지, 상품 목록 페이지, 상품 상세 페이지, MY 페이지, 회사 소개 페이지 포함

**2. 상품 등록 및 관리**
- 20개 이상의 상품을 등록
- 상품 목록 페이지에는 게시 순서대로 상품을 표시
- 각 상품에는 상품명, 카테고리, 상품 이미지, 가격, 간단한 설명 등이 표시되며 여러 페이지로 나누어 표시

**3. 네비게이션바 및 푸터바**
- 네비게이션바에는 홈, 상품 목록, MY 페이지, 회사 소개, 로그인이 포함
- 푸터바에는 회사 주소 및 고객센터 전화번호 등이 표시

**4. 계정 관리**
- 구글 계정과 이메일을 통한 로그인 및 이메일을 통한 회원가입
- 최소 3명 이상의 회원이 가입하도록 함

**5. 상품 상세 페이지**
- 각 상품의 내용을 자세히 보여주며, 상품의 자세한 설명은 Markdown으로 작성

**6. 상품 등록 및 수정 페이지**
- Superuser와 staff만이 상품을 등록 및 수정 가능
- 상품 등록 및 수정 페이지에는 crispy-form을 사용한 폼이 제공

**7. 홈 페이지**
- 쇼핑몰을 대표하는 이미지와 멘트를 표시
- 최근 게시된 상품 3개를 이미지, 상품명, 가격 등과 함께 표시

**8. 회사 소개 페이지**
- 쇼핑몰에 대한 소개를 표시
- 상품에 대한 통계 정보를 Bootstrap의 그래프를 이용하여 모달창으로 표시
  - 통계 정보의 예는 카테고리 별 상품의 갯수 등으로 함

**9. MY 페이지**
- 로그인한 사용자에게 username과 이메일을 표시.
- 사용자가 작성한 댓글을 표시하고, 댓글을 클릭하면 댓글이 달린 상품 상세 페이지로 이동.

**10. 댓글 기능**
- 상품 상세 페이지에 댓글을 표시
- 로그인한 모든 사용자는 댓글을 작성할 수 있도록 함

**11. 카테고리 및 검색 페이지**
- 각 카테고리에 포함된 상품을 보여주는 페이지 제공
- 상품명으로 검색 가능하며, 검색된 상품을 표시

**12. 사용자 및 댓글 작성자 아바타**
- 사용자와 댓글 작성자의 아바타를 페이지에 표시

**13. 데이터베이스**
- PostgreSQL을 사용하여 데이터베이스 관리
